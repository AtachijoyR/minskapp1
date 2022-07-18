<script lang="ts">
	import {navigate} from "svelte-routing";
	import axios from 'axios';
	import Swal from "sweetalert2";
	import {FormGroup, 
		Input, 
		Label, 
		Toast, 
		ToastHeader, 
		ToastBody, 
		Icon
	} from 'sveltestrap';
  
	let petName = "";
	let petBreed = "";
	let petAgeMonths = "";
	let petWeight = "";
	let petStatus = "";
	let petSpecie = "";
	let petRutOwner = "";
	let petDescription = "";  
	let error = null;

  /**
   * Función que modifica variable petStatus,
   * según estado del animal a registrar.
   * 
   */
  function modifiyStatus() {
    if (petStatus == "Sano") petStatus = '0';
    else if (petStatus == "En observación") petStatus = '1';
    else if (petStatus == "En pabellón") petStatus = '2';
    else if (petStatus == "Otro") petStatus = '3';
  }

  
  /**
   * Función que envía datos del animal a registrar al
   * backend, con sus respectivo datos.
  */
  async function sendPets() {
    
    modifiyStatus()
    try {
      const response = await axios.post('http://127.0.0.1:8000/Registrar-Mascotas/', {
        
        name: petName,
        breed: petBreed,
        age_months: petAgeMonths,
        weight: petWeight,
        status: '0',
        specie: petSpecie,
        rut_owner: petRutOwner,
        description: petDescription
      });
      navigate('/');
    } catch(e) {
      error = e
    }
  }
	
</script>

{#if error !== null}
  {error}
{:else}
<div class="d-grid bg-info gap-2 col-6 mx-auto">
  <div class="d-grid bg-info gap-2 col-6 mx-auto" >
    <Toast class="me-1">
      <ToastHeader>
        <h1>Registrar Mascota <Icon name="pencil-fill" /></h1>
        </ToastHeader>
      <ToastBody>
            <form id="form" method="POST">
                <FormGroup>
                <Label for="name">Nombre de la Mascota</Label>
                <Input bind:value={petName} placeholder="Ingrese nombre"/>
                </FormGroup>

                <FormGroup>
                <Label for="breed">Raza</Label>
                <Input bind:value={petBreed} placeholder="Ingrese raza"/>
                </FormGroup>

                <FormGroup>
                <Label for="specie">Especie</Label>
                <Input bind:value={petSpecie} placeholder="Ingrese especie"/>
                </FormGroup>

                <FormGroup>
                <Label for="weight">Peso</Label>
                <Input bind:value={petWeight} placeholder="Ingrese peso"/>
                </FormGroup>
                
                <FormGroup>
                <Label for="age">Edad</Label>
                <Input bind:value={petAgeMonths} placeholder="Ingrese edad en meses"/>
                </FormGroup>

                <FormGroup>
                <Label for="rut">RUT dueño</Label>
                <Input bind:value={petRutOwner} placeholder="Ingrese RUT"/>
                </FormGroup>

                <FormGroup>
                  <Label for="status">Estado</Label>
                  <Input bind:value={petStatus} type="select" name="select" id="exampleSelect">
                    <option>Sano</option>
                    <option>En observación</option>
                    <option>En pabellón</option>
                    <option>Otro</option>
                  </Input>
                </FormGroup>

                <FormGroup>
                <Label for="description">Descripción</Label>
                <Input bind:value={petDescription} type="textarea" name="text" id="exampleDescription" />
                </FormGroup>

                <div class="d-grid gap-2 col-6 mx-auto">
                  <button id='button' class="btn btn-info" type="button"
                  on:click={() => {
                    Swal.fire({
                      title: '¿Está seguro de que los datos son correctos?',
                      text: 'Luego no podrá modificar los datos.',
                      icon: 'warning',
                      showCancelButton: true,
                      confirmButtonText: 'Sí',
                      cancelButtonText: 'No'
                    }).then(result => {
                      if (result.value) {
                        sendPets();
                        Swal.fire('Su mascota ha sido registrada con éxito!');
                      }
                      else if (result.dismiss === Swal.DismissReason.cancel) {
                        Swal.fire('Cancelado');
                      }
                    });
                  }}>
                    Registrar
                  </button>
              </div>
            </form>
      </ToastBody>
    </Toast>
  </div>
</div>
{/if}
