;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Recomendador de Autos -  con Top-3 jeje  
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; deffinicion de la plantilla de usuario      
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(deftemplate usuario
  (slot presupuesto)                           ; bajo, medio, alto
  (slot uso-diario)                            ; si/no
  (slot uso-familiar)                          ; si/no
  (slot necesita-economia-combustible)         ; si/no
  (slot necesita-espacio)                      ; si/no
  (slot ubicacion)                             ; ciudad, rural
  (slot clima-lluvioso)                        ; si/no
  (slot clima-frio)                            ; si/no
  (slot preferencia-tecnologia)                ; si/no
  (slot valora-seguridad)                      ; si/no
  (slot preferencia-suv)                       ; si/no
  (slot preferencia-electrico)                 ; si/no
  (slot kilometraje-anual-alto)                ; si/no
  (slot precio-combustible-alto)               ; si/no
  (slot valora-mantenimiento-bajo)             ; si/no
  (slot marca-preferida)                       ; toyota, honda, etc.
  (slot prioriza-valor-reventa)                ; si/no
  (slot disponibilidad-servicio-tecnico)       ; si/no
  (slot ruta-montanosa)                        ; si/no
  (slot distancia-diaria)                      ; número (km)
  (slot preferencia-estetica)                  ; si/no
  (slot necesita-baul-grande)                  ; si/no
  (slot vehiculo-actual-antiguo)               ; si/no
  (slot edad-comprador)                        ; número
  (slot tipo-combustible-preferido)            ; gasolina, diésel, híbrido
  (slot preferencia-transmision)               ; manual, automatica
  (slot frecuencia-viajes)                     ; baja, media, alta
  (slot uso-offroad)                           ; si/no
  (slot reputacion-seguridad-importante)       ; si/no
  (slot acceso-credito)                        ; si/no
  (slot importancia-sistema-infoentretenimiento); si/no
  (slot uso-trabajo)                           ; si/no
  (slot uso-viajes-largos)                     ; si/no
  (slot preferencia-color)                     ; negro, blanco, etc.
  (slot tipo-estacionamiento)                  ; reducido, amplio
  (slot preferencia-autos-nuevos)              ; si/no
  (slot consumo-preferido-l-100km)             ; número (litros/100km)
  (slot estrato-socioeconomico)                ; bajo, medio, medio-alto, alto
  (slot conocimiento-mecanico)                 ; bajo, medio, alto
  (slot tamano-familia)                        ; número
  (slot desea-asistente-manejo)                ; si/no
  (slot uso-fines-semana)                      ; si/no
  (slot sensibilidad-precio)                   ; si/no
  (slot interes-financiamiento)                ; si/no
  (slot preferencia-familiar)                  ; si/no
  (slot preferencia-diseno-moderno)            ; si/no
  (slot preferencia-sedan)                     ; si/no
  (slot preferencia-deportivo)                 ; si/no
  (slot preferencia-hibrido)                   ; si/no
  (slot preferencia-economico)                 ; si/no
  (slot preferencia-4x4)                       ; si/no
  (slot preferencia-auto-sedan)                ; si/no
  (slot necesita-sistema-navegacion)           ; si/no
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Plantilla para recolectar recomendaciones  
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(deftemplate recomendacion
  (slot texto))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Hechos iniciales del usuario               
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(deffacts hechos-del-usuario
  (usuario
    (presupuesto alto)
    (uso-diario no)
    (uso-familiar no)
    (necesita-economia-combustible no)
    (necesita-espacio no)
    (ubicacion rural)
    (clima-lluvioso no)
    (clima-frio si)
    (preferencia-tecnologia no)
    (valora-seguridad si)
    (preferencia-suv si)
    (preferencia-electrico si)
    (kilometraje-anual-alto no)
    (precio-combustible-alto no)
    (valora-mantenimiento-bajo no)
    (marca-preferida bmw)
    (prioriza-valor-reventa no)
    (disponibilidad-servicio-tecnico no)
    (ruta-montanosa no)
    (distancia-diaria 10)
    (preferencia-estetica no)
    (necesita-baul-grande no)
    (vehiculo-actual-antiguo no)
    (edad-comprador 45)
    (tipo-combustible-preferido híbrido)
    (preferencia-transmision manual)
    (frecuencia-viajes baja)
    (uso-offroad si)
    (reputacion-seguridad-importante no)
    (acceso-credito no)
    (importancia-sistema-infoentretenimiento no)
    (uso-trabajo no)
    (uso-viajes-largos no)
    (preferencia-color blanco)
    (tipo-estacionamiento amplio)
    (preferencia-autos-nuevos no)
    (consumo-preferido-l-100km 8.0)
    (estrato-socioeconomico alto)
    (conocimiento-mecanico alto)
    (tamano-familia 2)
    (desea-asistente-manejo no)
    (uso-fines-semana no)
    (sensibilidad-precio no)
    (interes-financiamiento no)
    (preferencia-familiar no)
    (preferencia-diseno-moderno no)
    (preferencia-sedan si)
    (preferencia-deportivo no)
    (preferencia-hibrido si)
    (preferencia-economico no)
    (preferencia-4x4 si)
    (preferencia-auto-sedan si)
    (necesita-sistema-navegacion no)
  )
)


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; reglas de recolección de recomendaciones   
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(defrule regla1
  (usuario (presupuesto bajo) (necesita-economia-combustible si))
  =>
  (assert (recomendacion (texto "Auto compacto económico. Considera Toyota, Hyundai o Kia."))))

(defrule regla2
  (usuario (presupuesto alto) (preferencia-suv si))
  =>
  (assert (recomendacion (texto "SUV premium. Marcas: Nissan, Honda, Mitsubishi."))))

(defrule regla3
  (usuario (valora-seguridad si) (reputacion-seguridad-importante si))
  =>
  (assert (recomendacion (texto "Modelos con 5 estrellas en seguridad (Toyota, Honda, Volkswagen)."))))

(defrule regla4
  (usuario (clima-lluvioso si) (ruta-montanosa si))
  =>
  (assert (recomendacion (texto "Vehículo AWD para montaña. Marcas: Mitsubishi, Subaru."))))

(defrule regla5
  (usuario (uso-trabajo si) (uso-viajes-largos si))
  =>
  (assert (recomendacion (texto "Motor diésel o híbrido (Ford, Nissan, Hyundai)."))))

(defrule regla6
  (usuario (prioriza-valor-reventa si) (marca-preferida toyota))
  =>
  (assert (recomendacion (texto "Toyota de alta demanda para reventa."))))

(defrule regla7
  (usuario (kilometraje-anual-alto si) (precio-combustible-alto si))
  =>
  (assert (recomendacion (texto "Híbrido o eléctrico (Toyota, Chevrolet, Renault)."))))

(defrule regla8
  (usuario (disponibilidad-servicio-tecnico no))
  =>
  (assert (recomendacion (texto "Evitar marcas sin soporte local en Perú."))))

(defrule regla9
  (usuario (tipo-estacionamiento reducido) (preferencia-suv si))
  =>
  (assert (recomendacion (texto "SUV compacto urbano (Kia, Honda, Volkswagen)."))))

(defrule regla10
  (usuario (preferencia-transmision automatica) (uso-viajes-largos si))
  =>
  (assert (recomendacion (texto "Transmisión CVT (Nissan, Honda, Subaru)."))))

(defrule regla11
  (usuario (edad-comprador ?e&:(< ?e 35)) (preferencia-estetica si))
  =>
  (assert (recomendacion (texto "Deportivo compacto (Ford, Hyundai, Peugeot)."))))

(defrule regla12
  (usuario (necesita-baul-grande si) (uso-familiar si))
  =>
  (assert (recomendacion (texto "Sedán grande o SUV (Chevrolet, Toyota, Hyundai)."))))

(defrule regla13
  (usuario (vehiculo-actual-antiguo si))
  =>
  (assert (recomendacion (texto "Bono de recambio (Toyota, Ford)."))))

(defrule regla14
  (usuario (acceso-credito si) (presupuesto medio))
  =>
  (assert (recomendacion (texto "Financiamiento en Nissan, Mitsubishi, Kia."))))

(defrule regla15
  (usuario (importancia-sistema-infoentretenimiento si))
  =>
  (assert (recomendacion (texto "Pantalla táctil y conectividad (Chevrolet, Volkswagen, Renault)."))))

(defrule regla16
  (usuario (uso-offroad no) (ruta-montanosa si))
  =>
  (assert (recomendacion (texto "SUV urbano AWD (Subaru, Mitsubishi)."))))

(defrule regla17
  (usuario (frecuencia-viajes alta) (valora-mantenimiento-bajo si))
  =>
  (assert (recomendacion (texto "Marca confiable y económica (Toyota, Honda, Suzuki)."))))

(defrule regla18
  (usuario (conocimiento-mecanico bajo))
  =>
  (assert (recomendacion (texto "Bajo mantenimiento (Toyota, Hyundai, Kia)."))))

(defrule regla19
  (usuario (preferencia-autos-nuevos si) (presupuesto bajo))
  =>
  (assert (recomendacion (texto "Opciones nuevas económicas (Kia, Suzuki, Hyundai)."))))

(defrule regla20
  (usuario (preferencia-color negro))
  =>
  (assert (recomendacion (texto "Modelos en negro (Ford, Chevrolet, Honda)."))))

(defrule regla21
  (usuario (uso-familiar si) (preferencia-suv si) (preferencia-tecnologia si))
  =>
  (assert (recomendacion (texto "SUV familiar con tecnología (Nissan, Toyota, Kia)."))))

(defrule regla22
  (usuario (tipo-estacionamiento reducido))
  =>
  (assert (recomendacion (texto "Vehículo compacto y maniobrable (Honda, Suzuki, Renault)."))))

(defrule regla23
  (usuario (preferencia-diseno-moderno si))
  =>
  (assert (recomendacion (texto "Diseño actual (Peugeot, Volkswagen, Ford)."))))

(defrule regla24
  (usuario (presupuesto bajo) (preferencia-suv si))
  =>
  (assert (recomendacion (texto "SUV económica (Hyundai, Suzuki, Renault)."))))

(defrule regla25
  (usuario (preferencia-electrico si))
  =>
  (assert (recomendacion (texto "Vehículos eléctricos (Renault, Hyundai, Nissan)."))))

(defrule regla26
  (usuario (presupuesto medio) (preferencia-suv si))
  =>
  (assert (recomendacion (texto "SUV de gama media (Mitsubishi, Chevrolet, Kia)."))))

(defrule regla27
  (usuario (preferencia-familiar si) (marca-preferida toyota))
  =>
  (assert (recomendacion (texto "Toyota para uso familiar (Toyota, Honda)."))))

(defrule regla28
  (usuario (necesita-baul-grande si) (preferencia-suv si))
  =>
  (assert (recomendacion (texto "SUV con gran maletero (Toyota, Chevrolet, Hyundai)."))))

(defrule regla29
  (usuario (clima-frio si))
  =>
  (assert (recomendacion (texto "Vehículo con calefacción (Subaru, Mitsubishi, Honda)."))))

(defrule regla30
  (usuario (presupuesto alto) (preferencia-transmision automatica))
  =>
  (assert (recomendacion (texto "Auto de lujo automático (BMW, Mercedes-Benz, Audi)."))))

(defrule regla31
  (usuario (uso-diario si) (preferencia-economico si))
  =>
  (assert (recomendacion (texto "Auto económico y confiable (Suzuki, Kia, Honda)."))))

(defrule regla32
  (usuario (preferencia-sedan si) (presupuesto medio))
  =>
  (assert (recomendacion (texto "Sedán de gama media (Hyundai, Nissan, Ford)."))))

(defrule regla33
  (usuario (preferencia-color blanco))
  =>
  (assert (recomendacion (texto "Modelos en blanco (Toyota, Chevrolet, Ford)."))))

(defrule regla34
  (usuario (edad-comprador ?e&:(>= ?e 40)))
  =>
  (assert (recomendacion (texto "Autos cómodos y accesibles (Toyota, Honda, Chevrolet)."))))

(defrule regla35
  (usuario (preferencia-hibrido si))
  =>
  (assert (recomendacion (texto "Vehículo híbrido (Toyota, Honda, Nissan)."))))

(defrule regla36
  (usuario (preferencia-economico si) (uso-diario si))
  =>
  (assert (recomendacion (texto "Auto económico para el día a día (Hyundai, Suzuki)."))))

(defrule regla37
  (usuario (presupuesto alto) (preferencia-4x4 si))
  =>
  (assert (recomendacion (texto "SUV 4x4 para aventuras (Toyota, Land Rover, Mitsubishi)."))))

(defrule regla38
  (usuario (presupuesto bajo) (preferencia-deportivo si))
  =>
  (assert (recomendacion (texto "Vehículo deportivo económico (Hyundai, Ford, Peugeot)."))))

(defrule regla39
  (usuario (frecuencia-viajes baja) (preferencia-auto-sedan si))
  =>
  (assert (recomendacion (texto "Sedán de bajo mantenimiento (Suzuki, Kia, Honda)."))))

(defrule regla40
  (usuario (necesita-sistema-navegacion si) (presupuesto medio))
  =>
  (assert (recomendacion (texto "Auto con navegación de gama media (Nissan, Mazda, Chevrolet)."))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; reglaa final: Muentra Top-3 recomendaciones  
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(defrule imprimir-top3
  (not (impreso))
  (recomendacion (texto ?t1))
  (recomendacion (texto ?t2&:(neq ?t2 ?t1)))
  (recomendacion (texto ?t3&:(and (neq ?t3 ?t1) (neq ?t3 ?t2))))
  =>
  (printout t crlf "=== TOP 3 RECOMENDACIONES ===" crlf)
  (printout t "1. " ?t1 crlf)
  (printout t "2. " ?t2 crlf)
  (printout t "3. " ?t3 crlf)
  (assert (impreso)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Fin del sistema de reglas                   
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
