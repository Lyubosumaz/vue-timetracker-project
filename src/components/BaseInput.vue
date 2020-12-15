<template>
    <label>{{ label }}</label>
    <input
        :placeholder="label"
        type="field"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
    >
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';

@Options({
    props: {
        label: {
            msg: String,
            default: '',
        },
        modelValue: {
            type: [String, Number],
            default: '',
        },
    },
})
export default class FormAddingTime extends Vue {
    msg!: string;
}
</script>

<style scoped></style>
