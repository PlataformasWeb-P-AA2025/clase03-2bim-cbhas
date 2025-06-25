# clase03-2bim
![image](https://github.com/user-attachments/assets/f8f9793e-8449-4ade-8e48-a9c89ce27e2c)
* Cuando no haya un atributo related_name en el modelo para poder hacer referencia a la FK tenemos que hacerlo llamando a la clase en minusculas junto a _set.all (e.numerotelefonico_set.all)

### 25 junio 2025
* La funcion `crear_numero_telefonico_estudiante` nos ayuda a crear un numero telefonico asociado ya a un estudiante sin tener que elegir a que estudiante hay que insertar el nuebo numero, y esto pasa ya que al momento de llamar al formulario `NumeroTelefonicoEstudianteForm` estamos llamando al objeto estudiante vinculado y despues de eso ocultando (`forms.widgets.HiddenInput()`) para que el usuario ya no eliga a estudiante quiere agregar el telefono.