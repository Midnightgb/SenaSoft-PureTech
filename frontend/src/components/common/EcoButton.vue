<script setup>
import { computed } from 'vue';

const props = defineProps({
  variant: {
    type: String,
    default: 'primary',
    validator: (value) => ['primary', 'secondary', 'outline'].includes(value)
  },
  size: {
    type: String,
    default: 'md',
    validator: (value) => ['sm', 'md', 'lg'].includes(value)
  },
  disabled: {
    type: Boolean,
    default: false
  }
});

const classes = computed(() => {
  const baseClasses = 'font-semibold rounded transition-colors duration-300 focus:outline-none focus:ring-2 focus:ring-offset-2';
  const sizeClasses = {
    sm: 'px-3 py-1 text-sm',
    md: 'px-4 py-2',
    lg: 'px-6 py-3 text-lg'
  };
  const variantClasses = {
    primary: 'bg-green-500 text-white hover:bg-green-600 focus:ring-green-500',
    secondary: 'bg-blue-500 text-white hover:bg-blue-600 focus:ring-blue-500',
    outline: 'bg-transparent border-2 border-green-500 text-green-500 hover:bg-green-50 focus:ring-green-500'
  };
  const disabledClasses = props.disabled ? 'opacity-50 cursor-not-allowed' : 'cursor-pointer';
  return `${baseClasses} ${sizeClasses[props.size]} ${variantClasses[props.variant]} ${disabledClasses}`;
});

defineExpose({
  props,
  classes
});
</script>

<template>
  <button :class="classes" :disabled="disabled">
    <slot></slot>
  </button>
</template>