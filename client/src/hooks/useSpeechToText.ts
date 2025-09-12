import { useState, useEffect } from 'react';

// Comprobamos si la API de reconocimiento de voz está disponible en el navegador.
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = SpeechRecognition ? new SpeechRecognition() : null;

export const useSpeechToText = () => {
    const [transcript, setTranscript] = useState('');
    const [isListening, setIsListening] = useState(false);
    const [error, setError] = useState('');

    useEffect(() => {
        if (!recognition) {
            setError("Speech Recognition is not supported by your browser.");
            return;
        }

        // Configuramos la API
        recognition.continuous = false; // Detenerse después de la primera frase
        recognition.interimResults = false; // No mostrar resultados parciales

        recognition.onstart = () => {
            setIsListening(true);
            setTranscript(''); // Limpiar la transcripción al empezar
        };

        recognition.onresult = (event: SpeechRecognitionEvent) => {
            const lastResult = event.results[event.results.length - 1];
            const text = lastResult[0].transcript;
            setTranscript(text);
        };

        recognition.onerror = (event: any) => {
            setError(event.error);
            setIsListening(false);
        };

        recognition.onend = () => {
            setIsListening(false);
        };

        // Función de limpieza al desmontar el componente
        return () => {
            recognition.stop();
        };
    }, []);

    const startListening = () => {
        if (isListening) return;
        try {
            recognition.start();
        } catch (e) {
            setError("Could not start listening. Please check your microphone and permissions.");
        }
    };

    const stopListening = () => {
        if (!isListening) return;
        recognition.stop();
    };

    return { transcript, isListening, startListening, stopListening, error };
};