from deepface import DeepFace
import cv2

def main():
    cam = cv2.VideoCapture(0)
   
    if not cam.isOpened():
        print("Error no se pudo abrir la camara")
        return

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Error no se pudo leer el frame de la camara")
            break

        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            emotion = result[0]['dominant_emotion']

            cv2.putText(frame, f"Emotion {emotion}", (30,50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 2)
        except Exception as e:
            print(f"Error en analisis {e}")

        cv2.imshow("Emotion Detector", frame)

        # Salir si presionas 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Salir si cierras la ventana con la X
        if cv2.getWindowProperty("Emotion Detector", cv2.WND_PROP_VISIBLE) < 1:
            break
       
    cam.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
