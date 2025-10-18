package com.example.doc.app;

import com.example.doc.core.DocumentProcessor;
import com.example.doc.core.Document;

import java.util.ServiceLoader;

public class MainApp {
    public static void main(String[] args) {
        ServiceLoader<DocumentProcessor> loader = ServiceLoader.load(DocumentProcessor.class);

        Document document = new Document("Tugas 5", "Ini adalah isi dokumen contoh.");

        for (DocumentProcessor processor : loader) {
            System.out.println("=== Menggunakan Processor: " + processor.getFormatName() + " ===");
            System.out.println(processor.process(document.getContent()));
            System.out.println();
        }
    }
}
