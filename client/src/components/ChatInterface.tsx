import { useEffect } from "react";
import { useSpeechToText } from "../hooks/useSpeechToText";
import { sendChatToAI } from "../api/api";

const ChatInterface = () => {
  const { transcript, isListening, startListening, stopListening, error } =
    useSpeechToText();

  // Esta función se activará cuando el usuario termine de hablar.
  const handleVoiceInput = async () => {
    if (transcript) {
      console.log("User said:", transcript);
      try {
        const aiResponse = await sendChatToAI(transcript);
        console.log("AI Response:", aiResponse.message);
        // Aquí puedes actualizar el estado de tu UI con la respuesta de la IA
      } catch (error) {
        console.error("Error during AI chat:", error);
      }
    }
  };

  useEffect(() => {
    handleVoiceInput();
  }, [transcript]);

  return (
    <div>
      <h2>Chat con la IA</h2>
      <p>Estado: {isListening ? "Escuchando..." : "Pulsa para hablar"}</p>
      <p>
        Texto transcrito: <strong>{transcript}</strong>
      </p>

      <button
        onClick={isListening ? stopListening : startListening}
        disabled={!!error}
      >
        {isListening ? "Detener" : "Empezar a Escuchar"}
      </button>
      {error && <p style={{ color: "red" }}>Error: {error}</p>}
    </div>
  );
};

export default ChatInterface;
