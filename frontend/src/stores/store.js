import {writable} from 'svelte/store';

function userStore(){
    const {subscribe,set} = writable(getStorageUser());


    return{
        subscribe,
        loginUser:(arg) => set(arg),
        logoutUser: () => set(null),
    }
}

export function setStorageUser(user){
    localStorage.setItem('user', JSON.stringify(user));
}

function getStorageUser(){
    return localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')) : null;

}

export const user = userStore();
