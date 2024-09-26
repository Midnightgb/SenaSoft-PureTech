<template>
    <div class="bg-white dark:bg-gray-800 shadow-lg rounded-lg overflow-hidden">
        <img :src="imgSrc" alt="Imagen de reciclaje" class="w-full h-48 object-cover" />
        <div class="p-6">
            <h3 class="text-xl font-semibold text-gray-800 dark:text-gray-100">{{ title }}</h3>
            <p class="mt-2 text-gray-600 dark:text-gray-300">{{ description }}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: "CategoryCard",
    props: {
        title: {
            type: String,
            required: true,
        },
        description: {
            type: String,
            required: true,
        },
        imgSrc: {
            type: String,
            required: true,
        },
    },
};
</script>

<style scoped>
/* Estilos opcionales para las tarjetas */
</style>f