<template>
    <div>
        <form action="POST">
            <input type="text" id="name">
        </form>
    </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';

@Options({
    props: {
        msg: String,
    },
})
export default class FormAddingTime extends Vue {
    msg!: string;
}
</script>

<style scoped></style>
