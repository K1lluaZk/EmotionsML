import cv2
from detectemotions import EmotionDetector
import config

def main():
    # 1. Inicialización
    cam = cv2.VideoCapture(0)
    detector = EmotionDetector()
    frame_count = 0
    last_emotion = "Iniciando..."

    if not cam.isOpened():
        print("Error: No se pudo acceder a la cámara.")
        return

    print("Presiona 'q' para salir.")

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        # 2. Lógica de Inferencia Selectiva (Optimización)
        # Solo procesamos la IA cada X frames (definido en config.py)
        if frame_count % config.FRAME_SKIP == 0:
            last_emotion = detector.analyze_frame(frame)
        
        frame_count += 1

        # 3. Visualización (UI)
        # Dibujamos el texto siempre, pero solo se actualiza cuando la IA corre
        cv2.putText(
            frame, 
            f"Emocion: {last_emotion}", 
            (30, 50), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            config.FONT_SCALE, 
            config.TEXT_COLOR, 
            2
        )

        cv2.imshow("Emotion Detector Pro", frame)

        # 4. Gestión de salida
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        # Verificar si la ventana se cerró manualmente
        if cv2.getWindowProperty("Emotion Detector Pro", cv2.WND_PROP_VISIBLE) < 1:
            break

    # 5. Limpieza de recursos
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()