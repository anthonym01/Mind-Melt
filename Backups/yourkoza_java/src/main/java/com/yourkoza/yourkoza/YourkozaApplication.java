package com.yourkoza.yourkoza;

import java.io.StringReader;
import java_cup.runtime.*;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class YourkozaApplication {

	public static void main(String[] args) {
		String input = "let x be equal to 42;";
        YorkozaLexer lexer = new YorkozaLexer(new StringReader(input));

        // Tokenize the input
        Symbol token;
        try {
            while ((token = lexer.next_token()).sym != sym.EOF) {
                // Print each token
                System.out.println("Token: " + token.toString());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
		//SpringApplication.run(YourkozaApplication.class, args);
	}

}
