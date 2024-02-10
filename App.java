package com.hackathon;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.*;
import java.util.*;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main(String[] args) {
        Map<Integer, String> questionStatement = new HashMap<>();
        Map<Integer, Map<Character, String>> answers = new HashMap<>();
        StringBuilder sb = new StringBuilder();
        Pattern question = Pattern.compile("([0-9]+),\"(.*)");
        Pattern optA = Pattern.compile("(A).\\s(.*)");
        Pattern optB = Pattern.compile("(B).\\s(.*)");
        Pattern optC = Pattern.compile("(C).\\s(.*)\\\",");
        try {
            BufferedReader bf = new BufferedReader(new FileReader("./Aviation Quiz.csv"));
            String str = bf.readLine(); //consume labels
            try {
                while(true) {
                    //read in lines of 4
                    //question line
                    Matcher qMatch = question.matcher(bf.readLine());
                    bf.readLine(); //consume Options:
                    Matcher aMatch = optA.matcher(bf.readLine());
                    Matcher bMatch = optB.matcher(bf.readLine());
                    Matcher cMatch = optC.matcher(bf.readLine());
                    Matcher[] matches = new Matcher[]{aMatch, bMatch, cMatch};
                    qMatch.matches();
                    int id = Integer.parseInt(qMatch.group(1));
                    questionStatement.put(id, qMatch.group(2));
                    Map<Character, String> answer = new HashMap<>();
                    answers.put(id, answer);
                    System.out.println(questionStatement.size());
                    for(Matcher m : matches) {
                        m.matches();
                        answer.put(m.group(1).charAt(0), m.group(2));
                    }
                }
            } catch (NullPointerException e) {
                //break;
            }
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        System.out.println(questionStatement);
    }
}
