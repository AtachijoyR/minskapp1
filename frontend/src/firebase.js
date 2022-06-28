
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyD7T3rQyUD6JhP5KvGrP7y5lqt33fC9JGw",
  authDomain: "svelte-router-14dfd.firebaseapp.com",
  projectId: "svelte-router-14dfd",
  storageBucket: "svelte-router-14dfd.appspot.com",
  messagingSenderId: "901507317281",
  appId: "1:901507317281:web:59c77edcfcd324ade8ad60"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

const auth = getAuth(app);

export {auth};