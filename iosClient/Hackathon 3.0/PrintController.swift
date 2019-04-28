//
//  PrintController.swift
//  Hackathon 3.0
//
//  Created by Alec Zhang on 28/4/19.
//  Copyright © 2019 Arise. All rights reserved.
//

import Foundation
import UIKit
import SwiftSocket

class PrintController: UIViewController {
    
    let port = Int32(8000)
    @IBOutlet weak var textView: UITextView!
    
    // Prints the current blockchain to the app.
    override func viewDidLoad() {
        super.viewDidLoad()
        let response = loadBlockchain()
        textView.text = response
        
    }
    
    // Collects blockchain data from the server.
    private func loadBlockchain() -> String {
        let client = TCPClient(address: "localhost", port: port)
        
        let message = "print"
        
        switch client.connect(timeout: 5) {
        case .success:
            if let response = sendRequest(string: message, using: client) {
                client.close()
                return response
                
                
            }
        case .failure:
            return ""
        }
        
        client.close()
        return ""
    }
    
    private func sendRequest(string: String, using client: TCPClient) -> String? {
        
        switch client.send(string: string) {
        case .success:
            return readResponse(from: client)
        case .failure(let error):
            return nil
        }
    }
    
    private func readResponse(from client: TCPClient) -> String? {
        guard let response = client.read(1024*10, timeout: 2000) else { return nil }
        
        return String(bytes: response, encoding: .utf8)
    }
    
}
