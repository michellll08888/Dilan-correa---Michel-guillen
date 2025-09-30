# cajero.py

from FuncionesATM import (
    verificar_pin, 
    consultar_saldo, 
    retiro, 
    pago_clave_primera_vez, 
    CUENTAS
)

def obtener_input(mensaje, longitud_requerida=None):
    """Función de utilidad simple para obtener entrada de usuario."""
    while True:
        entrada = input(mensaje).strip()
        if entrada.isdigit() and (longitud_requerida is None or len(entrada) == longitud_requerida):
            return entrada
        else:
            print("Entrada inválida. Asegúrese de que sea un número y tenga la longitud correcta.")

def iniciar_sesion():
    """Maneja el inicio de sesión y devuelve la cuenta si es exitoso."""
    print("\n--- INICIO DE SESIÓN ---")
    
    # Pedimos la cuenta y el PIN (usando 4 dígitos para simplificar)
    num_cuenta = obtener_input("Ingrese su Número de Cuenta (ej: 1111): ", 4)
    pin = obtener_input("Ingrese su PIN (4 dígitos): ", 4)
    
    if verificar_pin(num_cuenta, pin):
        print("✅ Autenticación exitosa.")
        return num_cuenta
    else:
        print("❌ Error de autenticación: Cuenta o PIN incorrecto.")
        return None

def main():
    """Lógica principal del cajero."""
    
    cuenta_activa = iniciar_sesion()
    
    if not cuenta_activa:
        return # Termina si el inicio de sesión falla

    while True:
        print("\n--- MENÚ CAJERO ---")
        print(f"Cuenta: {cuenta_activa}")
        print("1. Consultar Saldo")
        print("2. Retiro de Efectivo")
        print("3. Cambiar PIN")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            saldo = consultar_saldo(cuenta_activa)
            print(f"\nSu saldo actual es: ${saldo:,.2f}")
            
        elif opcion == '2':
            try:
                monto = float(obtener_input("Monto a retirar: "))
                if monto <= 0:
                    print("El monto debe ser positivo.")
                    continue
                    
                nuevo_saldo = retiro(cuenta_activa, monto)
                if nuevo_saldo is False:
                    print("❌ Error: Saldo insuficiente.")
                else:
                    print(f"✅ Retiro de ${monto:,.2f} exitoso. Nuevo saldo: ${nuevo_saldo:,.2f}")
            except ValueError:
                print("Monto no válido.")

        elif opcion == '3':
            nuevo_pin = obtener_input("Ingrese el nuevo PIN (4 dígitos): ", 4)
            pago_clave_primera_vez(cuenta_activa, nuevo_pin)
            print("✅ PIN actualizado exitosamente.")
            
        elif opcion == '4':
            print("\n¡Gracias por usar el cajero!")
            break
            
        else:
            print("Opción no válida. Inténtelo de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()