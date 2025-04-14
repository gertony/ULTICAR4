import io
import contextlib
from tkinter import *
from tkinter import ttk, messagebox
from clips import Environment


class VehiculosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Recomendación de Vehículos")
        self.root.geometry("900x700")
        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.create_widgets()
        self.profile = {}

    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=BOTH, expand=True)

        # Notebook (pestañas)
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=BOTH, expand=True)

        # Crear pestañas
        self.create_presupuesto_tab()
        self.create_uso_tab()
        self.create_preferencias_tab()
        self.create_necesidades_tab()
        self.create_condiciones_tab()
        self.create_perfil_tab()

        # Botón de recomendación
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=X, pady=10)

        ttk.Button(btn_frame, text="Obtener Recomendaciones",
                   command=self.get_recommendations).pack(side=RIGHT)

        ttk.Button(btn_frame, text="Limpiar Formulario",
                   command=self.clear_form).pack(side=LEFT)

        # Área de resultados
        self.result_text = Text(main_frame, wrap=WORD, height=10,
                                font=('Arial', 10), padx=5, pady=5)
        self.result_text.pack(fill=BOTH, expand=True)

        scrollbar = ttk.Scrollbar(self.result_text)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.result_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_text.yview)

    def create_presupuesto_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Presupuesto")

        frame = ttk.LabelFrame(tab, text="Presupuesto y Financiamiento", padding=10)
        frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # Presupuesto
        ttk.Label(frame, text="Nivel de presupuesto:").grid(row=0, column=0, sticky=W, pady=2)
        self.presupuesto = ttk.Combobox(frame, values=["bajo", "medio", "alto"], state="readonly")
        self.presupuesto.grid(row=0, column=1, sticky=EW, pady=2)

        # Sensibilidad precio
        ttk.Label(frame, text="Sensibilidad al precio:").grid(row=1, column=0, sticky=W, pady=2)
        self.sensibilidad_precio = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.sensibilidad_precio.grid(row=1, column=1, sticky=EW, pady=2)

        # Acceso a crédito
        ttk.Label(frame, text="Acceso a crédito:").grid(row=2, column=0, sticky=W, pady=2)
        self.acceso_credito = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.acceso_credito.grid(row=2, column=1, sticky=EW, pady=2)

        # Interés financiamiento
        ttk.Label(frame, text="Interés en financiamiento:").grid(row=3, column=0, sticky=W, pady=2)
        self.interes_financiamiento = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.interes_financiamiento.grid(row=3, column=1, sticky=EW, pady=2)

        # Estrato socioeconómico
        ttk.Label(frame, text="Estrato socioeconómico:").grid(row=4, column=0, sticky=W, pady=2)
        self.estrato_socioeconomico = ttk.Combobox(frame,
                                                   values=["bajo", "medio", "medio_alto", "alto"], state="readonly")
        self.estrato_socioeconomico.grid(row=4, column=1, sticky=EW, pady=2)

    def create_uso_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Uso")

        frame = ttk.LabelFrame(tab, text="Patrones de Uso", padding=10)
        frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # Uso diario
        ttk.Label(frame, text="Uso diario:").grid(row=0, column=0, sticky=W, pady=2)
        self.uso_diario = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.uso_diario.grid(row=0, column=1, sticky=EW, pady=2)

        # Uso familiar
        ttk.Label(frame, text="Uso familiar:").grid(row=1, column=0, sticky=W, pady=2)
        self.uso_familiar = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.uso_familiar.grid(row=1, column=1, sticky=EW, pady=2)

        # Distancia diaria
        ttk.Label(frame, text="Distancia diaria (km):").grid(row=2, column=0, sticky=W, pady=2)
        self.distancia_diaria = ttk.Entry(frame)
        self.distancia_diaria.grid(row=2, column=1, sticky=EW, pady=2)

        # Tamaño familia
        ttk.Label(frame, text="Tamaño de la familia:").grid(row=3, column=0, sticky=W, pady=2)
        self.tamano_familia = ttk.Entry(frame)
        self.tamano_familia.grid(row=3, column=1, sticky=EW, pady=2)

        # Frecuencia viajes
        ttk.Label(frame, text="Frecuencia de viajes:").grid(row=4, column=0, sticky=W, pady=2)
        self.frecuencia_viajes = ttk.Combobox(frame,
                                              values=["baja", "media", "alta"], state="readonly")
        self.frecuencia_viajes.grid(row=4, column=1, sticky=EW, pady=2)

        # Uso trabajo
        ttk.Label(frame, text="Uso para trabajo:").grid(row=5, column=0, sticky=W, pady=2)
        self.uso_trabajo = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.uso_trabajo.grid(row=5, column=1, sticky=EW, pady=2)

        # Uso viajes largos
        ttk.Label(frame, text="Uso en viajes largos:").grid(row=6, column=0, sticky=W, pady=2)
        self.uso_viajes_largos = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.uso_viajes_largos.grid(row=6, column=1, sticky=EW, pady=2)

        # Uso fines de semana
        ttk.Label(frame, text="Uso fines de semana:").grid(row=7, column=0, sticky=W, pady=2)
        self.uso_fines_semana = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.uso_fines_semana.grid(row=7, column=1, sticky=EW, pady=2)

    def create_preferencias_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Preferencias")

        frame = ttk.LabelFrame(tab, text="Preferencias del Usuario", padding=10)
        frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # Tipo de vehículo
        ttk.Label(frame, text="Preferencia SUV:").grid(row=0, column=0, sticky=W, pady=2)
        self.preferencia_suv = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.preferencia_suv.grid(row=0, column=1, sticky=EW, pady=2)

        ttk.Label(frame, text="Preferencia sedán:").grid(row=1, column=0, sticky=W, pady=2)
        self.preferencia_sedan = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.preferencia_sedan.grid(row=1, column=1, sticky=EW, pady=2)

        ttk.Label(frame, text="Preferencia deportivo:").grid(row=2, column=0, sticky=W, pady=2)
        self.preferencia_deportivo = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.preferencia_deportivo.grid(row=2, column=1, sticky=EW, pady=2)

        # Transmisión
        ttk.Label(frame, text="Transmisión preferida:").grid(row=3, column=0, sticky=W, pady=2)
        self.preferencia_transmision = ttk.Combobox(frame,
                                                    values=["manual", "automatica"], state="readonly")
        self.preferencia_transmision.grid(row=3, column=1, sticky=EW, pady=2)

        # Color
        ttk.Label(frame, text="Color preferido:").grid(row=4, column=0, sticky=W, pady=2)
        self.preferencia_color = ttk.Combobox(frame,
                                              values=["negro", "blanco", "gris", "rojo", "azul"], state="readonly")
        self.preferencia_color.grid(row=4, column=1, sticky=EW, pady=2)

        # Tecnología
        ttk.Label(frame, text="Prefiere tecnología avanzada:").grid(row=5, column=0, sticky=W, pady=2)
        self.preferencia_tecnologia = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.preferencia_tecnologia.grid(row=5, column=1, sticky=EW, pady=2)

        # Estética
        ttk.Label(frame, text="Valora estética del vehículo:").grid(row=6, column=0, sticky=W, pady=2)
        self.preferencia_estetica = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.preferencia_estetica.grid(row=6, column=1, sticky=EW, pady=2)

        # Marca preferida
        ttk.Label(frame, text="Marca preferida:").grid(row=7, column=0, sticky=W, pady=2)
        self.marca_preferida = ttk.Combobox(frame,
                                            values=["toyota", "honda", "ford", "chevrolet", "nissan", "hyundai", "kia",
                                                    "bmw"],
                                            state="readonly")
        self.marca_preferida.grid(row=7, column=1, sticky=EW, pady=2)

        # Tipo combustible
        ttk.Label(frame, text="Combustible preferido:").grid(row=8, column=0, sticky=W, pady=2)
        self.tipo_combustible_preferido = ttk.Combobox(frame,
                                                       values=["gasolina", "diésel", "híbrido", "eléctrico"],
                                                       state="readonly")
        self.tipo_combustible_preferido.grid(row=8, column=1, sticky=EW, pady=2)

        # Preferencia familiar
        ttk.Label(frame, text="Prefiere vehículo familiar:").grid(row=9, column=0, sticky=W, pady=2)
        self.preferencia_familiar = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.preferencia_familiar.grid(row=9, column=1, sticky=EW, pady=2)

    def create_necesidades_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Necesidades")

        frame = ttk.LabelFrame(tab, text="Necesidades Específicas", padding=10)
        frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # Espacio
        ttk.Label(frame, text="Necesita espacio adicional:").grid(row=0, column=0, sticky=W, pady=2)
        self.necesita_espacio = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.necesita_espacio.grid(row=0, column=1, sticky=EW, pady=2)

        # Baúl grande
        ttk.Label(frame, text="Necesita baúl grande:").grid(row=1, column=0, sticky=W, pady=2)
        self.necesita_baul_grande = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.necesita_baul_grande.grid(row=1, column=1, sticky=EW, pady=2)

        # Seguridad
        ttk.Label(frame, text="Valora seguridad:").grid(row=2, column=0, sticky=W, pady=2)
        self.valora_seguridad = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.valora_seguridad.grid(row=2, column=1, sticky=EW, pady=2)

        # Mantenimiento
        ttk.Label(frame, text="Valora bajo mantenimiento:").grid(row=3, column=0, sticky=W, pady=2)
        self.valora_mantenimiento_bajo = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.valora_mantenimiento_bajo.grid(row=3, column=1, sticky=EW, pady=2)

        # Economía combustible
        ttk.Label(frame, text="Necesita economía de combustible:").grid(row=4, column=0, sticky=W, pady=2)
        self.necesita_economia_combustible = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.necesita_economia_combustible.grid(row=4, column=1, sticky=EW, pady=2)

        # Infoentretenimiento
        ttk.Label(frame, text="Valora sistema infoentretenimiento:").grid(row=5, column=0, sticky=W, pady=2)
        self.importancia_sistema_infoentretenimiento = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.importancia_sistema_infoentretenimiento.grid(row=5, column=1, sticky=EW, pady=2)

        # Diseño moderno
        ttk.Label(frame, text="Prefiere diseño moderno:").grid(row=6, column=0, sticky=W, pady=2)
        self.preferencia_diseno_moderno = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.preferencia_diseno_moderno.grid(row=6, column=1, sticky=EW, pady=2)

        # Asistente de manejo
        ttk.Label(frame, text="Desea asistente de manejo:").grid(row=7, column=0, sticky=W, pady=2)
        self.desea_asistente_manejo = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.desea_asistente_manejo.grid(row=7, column=1, sticky=EW, pady=2)

        # Sistema navegación
        ttk.Label(frame, text="Necesita sistema navegación:").grid(row=8, column=0, sticky=W, pady=2)
        self.necesita_sistema_navegacion = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.necesita_sistema_navegacion.grid(row=8, column=1, sticky=EW, pady=2)

    def create_condiciones_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Condiciones")

        frame = ttk.LabelFrame(tab, text="Condiciones de Uso", padding=10)
        frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # Ubicación
        ttk.Label(frame, text="Ubicación principal:").grid(row=0, column=0, sticky=W, pady=2)
        self.ubicacion = ttk.Combobox(frame, values=["ciudad", "rural"], state="readonly")
        self.ubicacion.grid(row=0, column=1, sticky=EW, pady=2)

        # Clima
        ttk.Label(frame, text="Clima lluvioso:").grid(row=1, column=0, sticky=W, pady=2)
        self.clima_lluvioso = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.clima_lluvioso.grid(row=1, column=1, sticky=EW, pady=2)

        ttk.Label(frame, text="Clima frío:").grid(row=2, column=0, sticky=W, pady=2)
        self.clima_frio = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.clima_frio.grid(row=2, column=1, sticky=EW, pady=2)

        # Rutas
        ttk.Label(frame, text="Ruta montañosa:").grid(row=3, column=0, sticky=W, pady=2)
        self.ruta_montanosa = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.ruta_montanosa.grid(row=3, column=1, sticky=EW, pady=2)

        # Estacionamiento
        ttk.Label(frame, text="Tipo de estacionamiento:").grid(row=4, column=0, sticky=W, pady=2)
        self.tipo_estacionamiento = ttk.Combobox(frame, values=["reducido", "amplio"], state="readonly")
        self.tipo_estacionamiento.grid(row=4, column=1, sticky=EW, pady=2)

        # Precio combustible
        ttk.Label(frame, text="Precio combustible alto:").grid(row=5, column=0, sticky=W, pady=2)
        self.precio_combustible_alto = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.precio_combustible_alto.grid(row=5, column=1, sticky=EW, pady=2)

        # Vehículo actual
        ttk.Label(frame, text="Vehículo actual antiguo:").grid(row=6, column=0, sticky=W, pady=2)
        self.vehiculo_actual_antiguo = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.vehiculo_actual_antiguo.grid(row=6, column=1, sticky=EW, pady=2)

        # Uso offroad
        ttk.Label(frame, text="Uso offroad:").grid(row=7, column=0, sticky=W, pady=2)
        self.uso_offroad = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.uso_offroad.grid(row=7, column=1, sticky=EW, pady=2)

        # Reputación seguridad
        ttk.Label(frame, text="Reputación seguridad importante:").grid(row=8, column=0, sticky=W, pady=2)
        self.reputacion_seguridad_importante = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.reputacion_seguridad_importante.grid(row=8, column=1, sticky=EW, pady=2)

        # Disponibilidad servicio técnico
        ttk.Label(frame, text="Disponibilidad servicio técnico:").grid(row=9, column=0, sticky=W, pady=2)
        self.disponibilidad_servicio_tecnico = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.disponibilidad_servicio_tecnico.grid(row=9, column=1, sticky=EW, pady=2)

    def create_perfil_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Perfil")

        frame = ttk.LabelFrame(tab, text="Perfil del Usuario", padding=10)
        frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # Edad
        ttk.Label(frame, text="Edad del comprador:").grid(row=0, column=0, sticky=W, pady=2)
        self.edad_comprador = ttk.Entry(frame)
        self.edad_comprador.grid(row=0, column=1, sticky=EW, pady=2)

        # Conocimiento mecánico
        ttk.Label(frame, text="Conocimiento mecánico:").grid(row=1, column=0, sticky=W, pady=2)
        self.conocimiento_mecanico = ttk.Combobox(frame,
                                                  values=["bajo", "medio", "alto"], state="readonly")
        self.conocimiento_mecanico.grid(row=1, column=1, sticky=EW, pady=2)

        # Preferencia autos nuevos
        ttk.Label(frame, text="Prefiere autos nuevos:").grid(row=2, column=0, sticky=W, pady=2)
        self.preferencia_autos_nuevos = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.preferencia_autos_nuevos.grid(row=2, column=1, sticky=EW, pady=2)

        # Preferencia económico
        ttk.Label(frame, text="Prefiere vehículo económico:").grid(row=3, column=0, sticky=W, pady=2)
        self.preferencia_economico = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.preferencia_economico.grid(row=3, column=1, sticky=EW, pady=2)

        # Preferencia híbrido
        ttk.Label(frame, text="Prefiere híbrido:").grid(row=4, column=0, sticky=W, pady=2)
        self.preferencia_hibrido = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.preferencia_hibrido.grid(row=4, column=1, sticky=EW, pady=2)

        # Preferencia eléctrico
        ttk.Label(frame, text="Prefiere eléctrico:").grid(row=5, column=0, sticky=W, pady=2)
        self.preferencia_electrico = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.preferencia_electrico.grid(row=5, column=1, sticky=EW, pady=2)

        # Preferencia 4x4
        ttk.Label(frame, text="Prefiere 4x4:").grid(row=6, column=0, sticky=W, pady=2)
        self.preferencia_4x4 = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.preferencia_4x4.grid(row=6, column=1, sticky=EW, pady=2)

        # Preferencia auto sedán
        ttk.Label(frame, text="Prefiere auto sedán:").grid(row=7, column=0, sticky=W, pady=2)
        self.preferencia_auto_sedan = ttk.Combobox(frame, values=["si", "no"], state="readonly")
        self.preferencia_auto_sedan.grid(row=7, column=1, sticky=EW, pady=2)

        # Consumo preferido
        ttk.Label(frame, text="Consumo preferido (l/100km):").grid(row=8, column=0, sticky=W, pady=2)
        self.consumo_preferido = ttk.Entry(frame)
        self.consumo_preferido.grid(row=8, column=1, sticky=EW, pady=2)

    def collect_profile(self):
        """Recopila todos los datos del formulario"""
        try:
            self.profile = {
                'presupuesto': self.presupuesto.get(),
                'uso-diario': self.uso_diario.get(),
                'uso-familiar': self.uso_familiar.get(),
                'necesita-economia-combustible': self.necesita_economia_combustible.get(),
                'necesita-espacio': self.necesita_espacio.get(),
                'ubicacion': self.ubicacion.get(),
                'clima-lluvioso': self.clima_lluvioso.get(),
                'clima-frio': self.clima_frio.get(),
                'preferencia-tecnologia': self.preferencia_tecnologia.get(),
                'valora-seguridad': self.valora_seguridad.get(),
                'preferencia-suv': self.preferencia_suv.get(),
                'preferencia-electrico': self.preferencia_electrico.get(),
                'kilometraje-anual-alto': "si" if int(self.distancia_diaria.get()) > 20000 else "no",
                'precio-combustible-alto': self.precio_combustible_alto.get(),
                'valora-mantenimiento-bajo': self.valora_mantenimiento_bajo.get(),
                'marca-preferida': self.marca_preferida.get(),
                'prioriza-valor-reventa': "si" if self.preferencia_familiar.get() == "si" else "no",
                'disponibilidad-servicio-tecnico': self.disponibilidad_servicio_tecnico.get(),
                'ruta-montanosa': self.ruta_montanosa.get(),
                'distancia-diaria': self.distancia_diaria.get(),
                'preferencia-estetica': self.preferencia_estetica.get(),
                'necesita-baul-grande': self.necesita_baul_grande.get(),
                'vehiculo-actual-antiguo': self.vehiculo_actual_antiguo.get(),
                'edad-comprador': self.edad_comprador.get(),
                'tipo-combustible-preferido': self.tipo_combustible_preferido.get(),
                'preferencia-transmision': self.preferencia_transmision.get(),
                'frecuencia-viajes': self.frecuencia_viajes.get(),
                'uso-offroad': self.uso_offroad.get(),
                'reputacion-seguridad-importante': self.reputacion_seguridad_importante.get(),
                'acceso-credito': self.acceso_credito.get(),
                'importancia-sistema-infoentretenimiento': self.importancia_sistema_infoentretenimiento.get(),
                'uso-trabajo': self.uso_trabajo.get(),
                'uso-viajes-largos': self.uso_viajes_largos.get(),
                'preferencia-color': self.preferencia_color.get(),
                'tipo-estacionamiento': self.tipo_estacionamiento.get(),
                'preferencia-autos-nuevos': self.preferencia_autos_nuevos.get(),
                'consumo-preferido-l-100km': self.consumo_preferido.get(),
                'estrato-socioeconomico': self.estrato_socioeconomico.get(),
                'conocimiento-mecanico': self.conocimiento_mecanico.get(),
                'tamano-familia': self.tamano_familia.get(),
                'desea-asistente-manejo': self.desea_asistente_manejo.get(),
                'uso-fines-semana': self.uso_fines_semana.get(),
                'sensibilidad-precio': self.sensibilidad_precio.get(),
                'interes-financiamiento': self.interes_financiamiento.get(),
                'preferencia-familiar': self.preferencia_familiar.get(),
                'preferencia-diseno-moderno': self.preferencia_diseno_moderno.get(),
                'preferencia-sedan': self.preferencia_sedan.get(),
                'preferencia-deportivo': self.preferencia_deportivo.get(),
                'preferencia-hibrido': self.preferencia_hibrido.get(),
                'preferencia-economico': self.preferencia_economico.get(),
                'preferencia-4x4': self.preferencia_4x4.get(),
                'preferencia-auto-sedan': self.preferencia_auto_sedan.get(),
                'necesita-sistema-navegacion': self.necesita_sistema_navegacion.get()
            }

            # Validar campos numéricos
            int(self.distancia_diaria.get())
            int(self.tamano_familia.get())
            int(self.edad_comprador.get())
            float(self.consumo_preferido.get())

            return True

        except ValueError as e:
            messagebox.showerror("Error", f"Por favor ingrese valores válidos en todos los campos:\n{str(e)}")
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Complete todos los campos del formulario:\n{str(e)}")
            return False

    def clear_form(self):
        """Limpia todos los campos del formulario"""
        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.Combobox):
                widget.set('')
            elif isinstance(widget, ttk.Entry):
                widget.delete(0, END)

        self.result_text.delete(1.0, END)
        self.profile = {}

    def run_profile(self, profile):
        """Ejecuta el motor de reglas CLIPS con el perfil proporcionado"""
        env = Environment()
        env.load('autos.clp')
        env.reset()

        # Construye y aserta el hecho usuario
        slots = []
        for key, value in profile.items():
            slots.append(f'({key} {value})')
        fact = f'(usuario {" ".join(slots)})'
        env.assert_string(fact)

        # Captura la salida
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            env.run()

        return output.getvalue()

    def get_recommendations(self):
        """Obtiene las recomendaciones basadas en los datos ingresados"""
        if not self.collect_profile():
            return

        self.result_text.delete(1.0, END)
        self.result_text.insert(END, "=== Procesando sus preferencias... ===\n\n")
        self.root.update()  # Actualizar la interfaz

        try:
            recommendations = self.run_profile(self.profile)
            self.result_text.insert(END, recommendations)
            self.result_text.insert(END, "\n\n=== Fin de las recomendaciones ===")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al procesar las reglas:\n{str(e)}")


if __name__ == '__main__':
    root = Tk()
    app = VehiculosApp(root)
    root.mainloop()
