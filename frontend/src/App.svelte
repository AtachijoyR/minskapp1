<script>
    import { Router, Link, Route } from "svelte-routing";
	import Home from './views/Home.svelte'
	import About from './views/About.svelte'
	import Profile from './views/Profile.svelte'
</script>

<div>
	<Router>
		<nav>
			<Link to="/">HOME</Link>
			<Link to="/about">About</Link>
			<Link to="/profile">Perfil</Link>
		</nav>

		<Route path = "/">
			<Home></Home>
		</Route>

		<Route path = "/about">
			<About></About>
		</Route>

		<Route path = "/profile">
			<Profile></Profile>
		</Route>
	</Router>



</div>



<style>

</style>