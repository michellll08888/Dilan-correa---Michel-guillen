# funciones.py

# Datos de prueba simplificados: {Número_Cuenta: [Saldo, PIN]}
CUENTAS = {
    '1111': [1000.00, '1234'], 
    '2222': [500.00, '4321']
}

def verificar_pin(num_cuenta, pin):
    """
    Verifica las credenciales de la cuenta.
    """
    if num_cuenta in CUENTAS and CUENTAS[num_cuenta][1] == pin:
        return True
    return False

def consultar_saldo(num_cuenta):
    """
    Devuelve el saldo actual de la cuenta.
    """
    return CUENTAS[num_cuenta][0]

def retiro(num_cuenta, monto):
    """
    Realiza un retiro y devuelve el nuevo saldo o False si falla.
    """
    saldo_actual = CUENTAS[num_cuenta][0]

    if monto > saldo_actual:
        return False  # Saldo insuficiente
    
    # Realizar el retiro
    CUENTAS[num_cuenta][0] -= monto
    return CUENTAS[num_cuenta][0]

def pago_clave_primera_vez(num_cuenta, nuevo_pin):
    """
    Establece un nuevo PIN para la cuenta.
    (En esta versión, no verifica si es "primera vez", simplemente lo cambia)
    """
    # Actualizar el PIN en la base de datos
    CUENTAS[num_cuenta][1] = nuevo_pin
    return True 