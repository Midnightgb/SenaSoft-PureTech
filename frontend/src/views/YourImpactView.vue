<template>
    <div class="flex flex-col h-screen w-screen bg-green-50">
        <header class="p-4 bg-green-500 text-white flex items-center">
        <ArrowLeftIcon class="h-6 w-6 mr-2" />
        <h1 class="text-xl font-bold">Your Impact</h1>
      </header>
      <main class="flex-1 overflow-auto p-4">
        <div class="bg-white rounded-lg p-4 shadow mb-4">
          <h2 class="text-lg font-semibold mb-2">Total Impact</h2>
          <div class="grid grid-cols-2 gap-4">
            <div class="text-center">
              <p class="text-3xl font-bold text-green-500">50 kg</p>
              <p class="text-sm text-gray-500">CO2 Avoided</p>
            </div>
            <div class="text-center">
              <p class="text-3xl font-bold text-green-500">5</p>
              <p class="text-sm text-gray-500">Trees Saved</p>
            </div>
          </div>
        </div>
        <div class="bg-white rounded-lg p-4 shadow mb-4">
          <h2 class="text-lg font-semibold mb-2">Recycling Breakdown</h2>
          <div class="h-40 bg-gray-200 flex items-center justify-center">
            <span class="text-gray-500">Pie Chart Placeholder</span>
          </div>
        </div>
        <div class="bg-white rounded-lg p-4 shadow mb-4">
          <h2 class="text-lg font-semibold mb-2">Community Impact</h2>
          <div class="h-40 bg-gray-200 flex items-center justify-center">
            <span class="text-gray-500">Bar Graph Placeholder</span>
          </div>
        </div>
        <button class="w-full bg-blue-500 text-white p-2 rounded-md font-medium flex items-center justify-center">
          <Share2Icon class="h-5 w-5 mr-2" />
          Share Your Impact
        </button>
      </main>
    </div>
</template>
 