<script lang="ts">
	import { Form, FormGroup, FormText, Input, Label } from 'sveltestrap';
	let radioGroup;
  </script>
  <h1>Registrar Mascota</h1>
  <Form>
	<FormGroup>
	  <Label for="name">Nombre de la Mascota</Label>
	  <Input placeholder="Ingrese nombre" />
	</FormGroup>
	<FormGroup>
	  <Label for="breed">Raza</Label>
	  <Input
		placeholder="Ingrese raza"
	  />
	</FormGroup>
	<FormGroup>
	  <Label for="specie">Especie</Label>
	  <Input 
		placeholder="Ingrese especie"
	  />
	</FormGroup>
	<FormGroup>
	  <Label for="weight">Peso</Label>
	  <Input
		placeholder="Ingrese peso"
	  />
	</FormGroup>
	
	<FormGroup>
	  <Label for="age">Edad</Label>
	  <Input
		placeholder="Ingrese edad en meses"
	  />
	</FormGroup>
	<FormGroup>
	  <Label for="rut">RUT dueño</Label>
	  <Input
		placeholder="Ingrese RUT"
	  />
	</FormGroup>

	<FormGroup>
	  <Label for="status">Estado</Label>
	  <Input type="select" name="select" id="exampleSelect"> 
		<option>Sano</option>
		<option>En observación</option>
		<option>En pabellón</option>
		<option>Otro</option>
	  </Input>
	</FormGroup>

	<FormGroup>
	  <Label for="description">Descripción</Label>
	  <Input type="textarea" name="text" id="exampleDescription" />
	</FormGroup>
	
  </Form>