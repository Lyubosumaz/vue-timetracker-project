<template>
    <FormAddingTime />
    <img alt="Vue logo" src="../assets/images/logo.png" />
    <FourOFour msg="Welcome to Your Vue.js + TypeScript App" />
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import FourOFour from '../components/FourOFour.vue';
import FormAddingTime from '../components/FormAddingTime.vue';

@Options({
    components: {
        FourOFour,
        FormAddingTime,
    },
})
export default class App extends Vue {}
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
</style>
