import torch
from torchvision import transforms
from torchvision.transforms.functional import to_pil_image
from PIL import Image
from torch.serialization import add_safe_globals
from torch.nn import Sequential

# Permitir que 'Sequential' sea cargado
add_safe_globals([Sequential])


# Dispositivo
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Clases
classes = ['Árbol Muerto', 'Muérdago', 'Urbano', 'Vegetacion']

# Transformaciones de entrada
transform_pipeline = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Función para cargar el modelo
def load_model(model_path='module/model/Model_DenseNet.pt'):
    model = torch.load(model_path, map_location=device, weights_only=False)
    model = model.to(device)  # Asegura que el modelo esté en el dispositivo
    model.eval()
    return model

# Función para predecir la clase de la imagen
def predict_image_class(image_file):
    try:
        # Carga del modelo
        model = load_model()

        # Verifica si el archivo temporal es leído y convertido a imagen PIL
        image_pil = Image.open(image_file).convert("RGB")

        # Aplica transformaciones a la imagen
        image_tensor = transform_pipeline(image_pil)
        image_tensor = image_tensor.unsqueeze(0).to(device)  # Agrega una dimensión y envía al dispositivo

        # Predicción sin gradientes
        with torch.no_grad():
            output = model(image_tensor)
            _, predicted = torch.max(output, 1)
            predicted_class = classes[predicted.item()]

        # Clasificación binaria para 'Muérdago'
        return 1 if predicted_class == 'Muérdago' else 0

    except Exception as e:
        print(f"Error en la predicción: {e}")
        return e
