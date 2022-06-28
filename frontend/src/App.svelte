<script>
    import { Router, Link, Route } from "svelte-routing";
	import Home from './views/Home.svelte'
	import Login from './views/Login.svelte'
	import Contact from './views/Contact.svelte'
	import Register from './views/Register.svelte'
	import Search from './views/Search.svelte'
	import Logout from "./views/Logout.svelte";
	import Visualizar from "./views/Visualizar.svelte"
	import {user} from "./stores/store";
</script>

<div>
	<Router>
		<nav>
			<div class="left_div">
				<nav>
					<Link to="/">CliniPet</Link>
				</nav>
			</div>
			<div class="right_div">
				<nav>
					{#if $user}
						<Link to ="/contact">About</Link>
						&nbsp&nbsp;
						<Link to="/logout">Cerrar sesion</Link>
					{/if}
				</nav>
			</div>
			<div class="right_div">
				<nav>
					{#if !$user}
						<Link to="/login">Iniciar Sesión</Link>
					{/if}
					&nbsp&nbsp;
				</nav>
			</div>
		</nav>

		<Route path = "/">
			<Home></Home>
		</Route>

		<Route path = "/login">
			<Login></Login>
		</Route>

		<Route path = "/register">
			<Register></Register>
		</Route>

		<Route path = "/searchPet">
			<Search></Search>
		</Route>

		<Route path = "/contact">
			<Contact></Contact>
		</Route>

		<Route path = "/logout">
			<Logout></Logout>
		</Route>

		<Route path = "/visualizar">
			<Visualizar></Visualizar>
		</Route>
		
	</Router>

</div>

<style>
    nav {
		display: flex;
	}
	nav div {
		flex: 1;
		padding: 1rem;
	}
    .left_div {
		text-align: left;
		background-color: #71cf97c4;		
        font-weight: bolder;
	}
	.right_div {
		background-color: rgba(149, 149, 149, 0.292);        
        max-width: 210px;
        text-align: right;
        font-weight: bolder;
	}
</style>