<script lang="ts">
	import { Form, FormGroup, FormText, Input, Label, Toast, ToastHeader, ToastBody, Icon, Button} from 'sveltestrap';
	let radioGroup;

  </script>


<div aria-live="polite" aria-atomic="true" class="d-flex justify-content-center align-items-center" style="min-height: 600px;">
  <div class="p-3 bg-info mb-3" >
    <Toast class="me-1">
      <ToastHeader>
        <h1>Registrar Mascota <Icon name="pencil-fill" /></h1>
    </ToastHeader>
      <ToastBody>
 
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
            <div>
                <Button>INGRESAR</Button>
            </div>
      </ToastBody>
    </Toast>
  </div>
</div>


