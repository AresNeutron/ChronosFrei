// global.d.ts
interface Window {
    SpeechRecognition: any;
    webkitSpeechRecognition: any;
}

interface SpeechRecognitionEvent extends Event {
    results: {
        transcript: string;
    }[][];
}