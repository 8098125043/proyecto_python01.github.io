class Ticket:
    def __init__(self, id, cliente, asunto, estado="Abierto", agente_asignado=None):
        self.id = id
        self.cliente = cliente
        self.asunto = asunto
        self.estado = estado
        self.agente_asignado = agente_asignado

    def __str__(self):
        return f"ID: {self.id}, Cliente: {self.cliente}, Asunto: {self.asunto}, Estado: {self.estado}, Agente Asignado: {self.agente_asignado}"


class TicketManager:
    def __init__(self):
        self.tickets = []
        self.next_id = 1

    def crear_ticket(self, cliente, asunto):
        ticket = Ticket(self.next_id, cliente, asunto)
        self.tickets.append(ticket)
        self.next_id += 1
        return ticket

    def listar_tickets(self):
        if not self.tickets:
            print("No hay tickets disponibles.")
        else:
            print("Lista de tickets:")
            for ticket in self.tickets:
                print(ticket)

    def buscar_tickets_por_cliente(self, cliente):
        encontrados = [ticket for ticket in self.tickets if ticket.cliente == cliente]
        if not encontrados:
            print(f"No se encontraron tickets para el cliente {cliente}.")
        else:
            print(f"Tickets para el cliente {cliente}:")
            for ticket in encontrados:
                print(ticket)

    def buscar_tickets_por_estado(self, estado):
        encontrados = [ticket for ticket in self.tickets if ticket.estado == estado]
        if not encontrados:
            print(f"No se encontraron tickets en estado {estado}.")
        else:
            print(f"Tickets en estado {estado}:")
            for ticket in encontrados:
                print(ticket)

    def asignar_agente(self, id_ticket, agente):
        ticket = self.buscar_ticket_por_id(id_ticket)
        if ticket:
            ticket.agente_asignado = agente
            print(f"Agente {agente} asignado al ticket {id_ticket}.")
        else:
            print(f"No se encontró ningún ticket con ID {id_ticket}.")

    def cerrar_ticket(self, id_ticket):
        ticket = self.buscar_ticket_por_id(id_ticket)
        if ticket:
            ticket.estado = "Cerrado"
            print(f"El ticket {id_ticket} ha sido cerrado.")
        else:
            print(f"No se encontró ningún ticket con ID {id_ticket}.")

    def buscar_ticket_por_id(self, id_ticket):
        for ticket in self.tickets:
            if ticket.id == id_ticket:
                return ticket
        return None


class TicketApp:
    def __init__(self):
        self.ticket_manager = TicketManager()

    def mostrar_menu(self):
        while True:
            print("\n--- Menú de Tickets ---")
            print("1. Crear un nuevo ticket")
            print("2. Listar todos los tickets")
            print("3. Asignar un agente a un ticket")
            print("4. Cerrar un ticket")
            print("5. Buscar tickets por cliente")
            print("6. Buscar tickets por estado")
            print("0. Salir")
            opcion = input("Ingrese el número de la opción que desea realizar: ")

            if opcion == "1":
                self.crear_ticket()
            elif opcion == "2":
                self.listar_tickets()
            elif opcion == "3":
                self.asignar_agente()
            elif opcion == "4":
                self.cerrar_ticket()
            elif opcion == "5":
                self.buscar_por_cliente()
            elif opcion == "6":
                self.buscar_por_estado()
            elif opcion == "0":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, ingrese un número válido.")

    def crear_ticket(self):
        cliente = input("Ingrese el nombre del cliente: ")
        asunto = input("Ingrese el asunto del ticket: ")
        self.ticket_manager.crear_ticket(cliente, asunto)
        print("Ticket creado con éxito.")

    def listar_tickets(self):
        self.ticket_manager.listar_tickets()

    def asignar_agente(self):
        id_ticket = int(input("Ingrese el ID del ticket que desea asignar: "))
        agente = input("Ingrese el nombre del agente: ")
        self.ticket_manager.asignar_agente(id_ticket, agente)

    def cerrar_ticket(self):
        id_ticket = int(input("Ingrese el ID del ticket que desea cerrar: "))
        self.ticket_manager.cerrar_ticket(id_ticket)

    def buscar_por_cliente(self):
        cliente = input("Ingrese el nombre del cliente: ")
        self.ticket_manager.buscar_tickets_por_cliente(cliente)

    def buscar_por_estado(self):
        estado = input("Ingrese el estado del ticket (Abierto/Cerrado): ")
        self.ticket_manager.buscar_tickets_por_estado(estado)

# Ejemplo de uso
if __name__ == "__main__":
    app = TicketApp()
    app.mostrar_menu()
