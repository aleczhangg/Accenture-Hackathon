//
//  ViewController.swift
//  Hackathon 3.0
//
//  Created by Jerry Jin on 27/4/19.
//  Copyright © 2019 Arise. All rights reserved.
//

import UIKit
import SwiftSocket

class Request: UIViewController, UITextFieldDelegate {
    
    let ourName = "Ticketek"
    let hostname = "localhost"
    let portNumber = Int32(8000)
    
    var error = 0
    @IBOutlet weak var ticketIDField: UITextField!
    @IBOutlet weak var ownerNameField: UITextField!
    @IBOutlet weak var resalePriceField: UITextField!
    @IBOutlet weak var textView: UITextView!
    
   // Main method.
    override func viewDidLoad() {
        super.viewDidLoad()
        // Alec's code.
        ticketIDField.delegate = self
        ownerNameField.delegate = self
        resalePriceField.delegate = self
        
        self.hideKeyboard()

    }
    
    // HELPER METHODS
    @IBAction func requestTapped(_ sender: Any) {
        // Error handling first.
        if ticketIDField.text?.isEmpty ?? true {
            let alert = UIAlertView()
            alert.title = "Error"
            alert.message = "Missing field"
            alert.addButton(withTitle: "Ok")
            alert.show()
            return
        } else if ownerNameField.text?.isEmpty ?? true {
            let alert = UIAlertView()
            alert.title = "Error"
            alert.message = "Missing field"
            alert.addButton(withTitle: "Ok")
            alert.show()
            return
        } else if resalePriceField.text?.isEmpty ?? true {
            let alert = UIAlertView()
            alert.title = "Error"
            alert.message = "Missing field"
            alert.addButton(withTitle: "Ok")
            alert.show()
            return
        }
        
        var inputPrice = resalePriceField.text!
        let sliced = String(inputPrice.dropFirst())
        
        let message = "transfer|" + (ticketIDField.text!) + "|" + ourName + "|" + (ownerNameField.text!) + "|" + (sliced)

        print(message)
        // Some actual client stuff.
        let client = TCPClient(address: hostname, port: portNumber)

        // Try and connect to the server.
        switch client.connect(timeout: 5) {
        case .success:
            appendToTextField(string: "Connected to host \(client.address)")
            if let response = sendRequest(string: message, using: client) {
                print("hello world")
                print(response)
                if response == "1" {
                    // Need to handle this?
                    performSegue(withIdentifier: "SuccessSegue", sender: nil)


                } else if response == "-1" {
                    // Need to handle this?
                    let alert = UIAlertView()
                    alert.title = "Error"
                    alert.message = "It appears that you don't own this ticket."
                    alert.addButton(withTitle: "Ok")
                    alert.show()
                }
                appendToTextField(string: "Response: \(response)")
            }
        case .failure:
            appendToTextField(string: "Error connecting to host.")
        }

        client.close()
    }
    
    private func sendRequest(string: String, using client: TCPClient) -> String? {
        appendToTextField(string: "Sending data ... ")
        
        switch client.send(string: string) {
        case .success:
            return readResponse(from: client)
        case .failure(let error):
            appendToTextField(string: String(describing: error))
            return nil
        }
    }
    
    private func readResponse(from client: TCPClient) -> String? {
        guard let response = client.read(1024*10, timeout: 2000) else { return nil }
        
        return String(bytes: response, encoding: .utf8)
    }
    
    private func appendToTextField(string: String) {
        textView.text.appending("\n\(string)")
    }
    
    // Jerry
//
//    @IBAction func showError(_ sender: Any) {
//        let alert = UIAlertController(title: "An unexpected error has occured", message: "Please try again", preferredStyle: .alert)
//
//        alert.addAction(UIAlertAction(title: "Ok", style: .default, handler: nil))
//
//        self.present(alert, animated: true)
//    }
    
} // end of class

// Hide keyboard function
extension UIViewController
{
    func hideKeyboard()
    {
        let tap: UITapGestureRecognizer = UITapGestureRecognizer(
            target: self,
            action: #selector(UIViewController.dismissKeyboard))
        
        tap.cancelsTouchesInView = false
        view.addGestureRecognizer(tap)
    }
    
    @objc func dismissKeyboard()
    {
        view.endEditing(true)
    }
}

// Alec
extension Request {
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        return true
    }
}


