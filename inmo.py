from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>InmoSecure - Portal Inmobiliario Cifrado</title>
    <style>
        body { 
            font-family: 'Segoe UI', sans-serif; 
            background-color: #0d1117; 
            color: #c9d1d9;
            display: flex; 
            flex-direction: column;
            align-items: center; 
            min-height: 100vh; 
            margin: 0; 
            padding: 20px;
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        h1 { color: #ff007f; margin-bottom: 5px; font-size: 2.5rem; text-shadow: 0 0 10px rgba(255, 0, 127, 0.3); }
        h2 { color: #00f5ff; border-bottom: 2px solid #ff007f; padding-bottom: 8px; }
        
        .security-badge { 
            font-size: 12px; 
            text-align: center; 
            color: #00f5ff; 
            background: rgba(0, 245, 255, 0.1); 
            padding: 8px 15px; 
            border-radius: 20px; 
            font-weight: bold; 
            border: 1px solid #00f5ff;
            display: inline-block;
            box-shadow: 0 0 15px rgba(0, 245, 255, 0.2);
        }
        
        .main-content {
            display: flex;
            gap: 30px;
            max-width: 900px;
            width: 100%;
            margin-top: 20px;
        }

        .info-panel {
            flex: 1;
            background: #161b22;
            padding: 25px;
            border-radius: 12px;
            border: 1px solid #30363d;
        }
        
        .property-card {
            background: #21262d;
            padding: 12px;
            margin-bottom: 12px;
            border-radius: 6px;
            border-left: 4px solid #00f5ff;
        }
        .property-card h4 { margin: 0 0 5px 0; color: #ffffff; }
        .property-card p { margin: 0; font-size: 13px; color: #8b949e; }

        .form-container { 
            width: 380px;
            background: #161b22; 
            padding: 35px; 
            border-radius: 12px; 
            border: 1px solid #30363d;
            box-shadow: 0 8px 24px rgba(0,0,0,0.3); 
        }
        
        label { font-size: 13px; color: #8b949e; font-weight: bold; display: block; margin-top: 15px; }
        input { 
            width: 100%; 
            padding: 12px; 
            margin: 6px 0; 
            background: #0d1117;
            border: 1px solid #30363d; 
            border-radius: 6px; 
            box-sizing: border-box; 
            color: #ffffff;
            font-size: 14px;
        }
        input:focus {
            outline: none;
            border-color: #ff007f;
            box-shadow: 0 0 8px rgba(255, 0, 127, 0.5);
        }
        
        button { 
            width: 100%; 
            padding: 14px; 
            background-color: #ff007f; 
            color: white; 
            border: none; 
            border-radius: 6px; 
            font-size: 16px; 
            cursor: pointer; 
            font-weight: bold; 
            margin-top: 20px;
            box-shadow: 0 4px 12px rgba(255, 0, 127, 0.3);
            transition: background 0.2s, transform 0.1s;
        }
        button:hover { background-color: #e0006c; transform: translateY(-1px); }
        button:active { transform: translateY(1px); }
        
        .success-box { 
            background-color: rgba(0, 245, 255, 0.1); 
            color: #00f5ff; 
            padding: 12px; 
            border-radius: 6px; 
            text-align: center; 
            margin-top: 20px; 
            font-size: 14px; 
            border: 1px solid #00f5ff; 
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🔒 InmoSecure Portal</h1>
        <div class="security-badge">Cifrado de Capa de Transporte (TLS/SSL) Activo</div>
    </div>
    
    <div class="main-content">
        <div class="info-panel">
            <h2>🏢 Catálogo de Inmuebles</h2>
            <p style="font-size: 14px; color: #8b949e;">Explora nuestras opciones disponibles para estudio financiero inmediato:</p>
            
            <div class="property-card">
                <h4>Apartamento Zona Norte</h4>
                <p>Valor: $350,000,000 | Área: 75m²</p>
            </div>
            <div class="property-card">
                <h4>Casa Campestre Suba</h4>
                <p>Valor: $680,000,000 | Área: 140m²</p>
            </div>
            <div class="property-card">
                <h4>Consultorio Médico Centro</h4>
                <p>Valor: $210,000,000 | Área: 45m²</p>
            </div>
        </div>

        <div class="form-container">
            <h3 style="margin-top: 0; color: #ffffff; text-align: center;">Estudio de Crédito Seguro</h3>
            <p style="font-size: 13px; color: #8b949e; text-align: center;">Los datos ingresados se transmitirán cifrados mediante HTTPS para proteger su privacidad financiera.</p>
            
            <form method="POST">
                <label>Nombre Completo:</label>
                <input type="text" name="nombre" placeholder="Ej. Sergio Fuentes" required>
                
                <label>Documento de Identidad:</label>
                <input type="text" name="cedula" placeholder="Número de identificación" required>
                
                <label>Ingresos Mensuales Certificados ($):</label>
                <input type="text" name="ingresos" placeholder="Ej. 4000000" required>
                
                <button type="submit">Enviar Solicitud Cifrada</button>
            </form>
            
            {% if mensaje %}
                <div class="success-box">{{ mensaje }}</div>
            {% endif %}
        </div>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    mensaje = None
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        mensaje = f"¡Transmisión Segura! Los datos de {nombre} han sido inyectados al túnel SSL/TLS y recibidos sin alteraciones."
    return render_template_string(HTML_TEMPLATE, mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True, port=5000, ssl_context=('certificados/cert.pem', 'certificados/key.pem'))
