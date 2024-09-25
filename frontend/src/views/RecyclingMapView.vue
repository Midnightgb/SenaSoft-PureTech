<template>
   <div class="flex flex-col h-screen w-screen bg-green-50">
    <header class="p-4 bg-green-500 text-white flex items-center">
        <ArrowLeftIcon class="h-6 w-6 mr-2" />
        <h1 class="text-xl font-bold">Recycling Map</h1>
      </header>
      <main class="flex-1 relative">
        <div class="absolute inset-0 bg-gray-200 flex items-center justify-center">
          <span class="text-gray-500">Map View</span>
        </div>
        <div class="absolute top-4 right-4 space-y-2">
          <button class="bg-white p-2 rounded-full shadow">
            <ListIcon class="h-6 w-6 text-gray-600" />
          </button>
          <button class="bg-white p-2 rounded-full shadow">
            <FilterIcon class="h-6 w-6 text-gray-600" />
          </button>
        </div>
        <div class="absolute bottom-4 left-4 right-4 bg-white rounded-lg shadow p-4">
          <h2 class="font-semibold mb-2">Nearest Recycling Point</h2>
          <div class="flex items-center">
            <MapPinIcon class="h-5 w-5 text-red-500 mr-2" />
            <span>123 Green Street, Eco City</span>
          </div>
          <p class="text-sm text-gray-500 mt-1">0.5 miles away</p>
          <button class="mt-2 w-full bg-green-500 text-white p-2 rounded-md font-medium">
            Get Directions
          </button>
        </div>
      </main>
    </div>
</template>
