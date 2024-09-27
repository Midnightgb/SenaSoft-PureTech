<template>
    <div class="min-h-screen bg-gray-100 dark:bg-gray-900 flex flex-col">
        <!-- Barra de navegación superior -->
        <NavbarC />

        <!-- Layout principal con barra lateral y contenido -->
        <div class="flex flex-1 overflow-hidden">
            <!-- Barra lateral izquierda para las categorías -->
            <SidebarC />

            <!-- Área de contenido principal -->
            <main class="flex-1 p-6">
                <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-100 mb-4">
                    Categorización de Reciclaje
                </h1>

                <p class="text-gray-600 dark:text-gray-300">
                    Aquí encontrarás información sobre cómo categorizar correctamente los diferentes tipos de materiales
                    reciclables, como plástico, papel, vidrio, y otros.
                </p>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-6">                    
                    <CategoryCard title="Plástico"
                        description="Botellas, envases, bolsas. Aprende a separar correctamente el plástico reciclable."
                        imgSrc="https://example.com/plastic.jpg" />

                    <CategoryCard title="Papel"
                        description="Periódicos, revistas, cajas. Aprende qué tipo de papel se puede reciclar."
                        imgSrc="https://example.com/paper.jpg" />

                    <CategoryCard title="Vidrio"
                        description="Botellas de vidrio, frascos. Descubre cómo se recicla el vidrio adecuadamente."
                        imgSrc="https://example.com/glass.jpg" />

                    <CategoryCard title="Metal"
                        description="Botellas, envases, bolsas. Aprende a separar correctamente el plástico reciclable."
                        imgSrc="https://example.com/plastic.jpg" />

                    <CategoryCard title="Órganicos"
                        description="Botellas, envases, bolsas. Aprende a separar correctamente el plástico reciclable."
                        imgSrc="https://example.com/plastic.jpg" />
                    
                </div>
            </main>
        </div>
    </div>
</template>

<script setup>
import NavbarC from "@/components/layout/NavbarC.vue";
import SidebarC from "@/components/layout/SidebarC.vue";
import CategoryCard from "@/components/CategoryCard.vue";


</script>

<style scoped>
/* Aquí puedes agregar estilos adicionales si es necesario */
</style>