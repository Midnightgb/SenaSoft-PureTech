<template>
    <div class="flex flex-col h-screen w-screen bg-green-50">
      <header class="p-4 bg-green-500 text-white flex items-center">
        <h1 class="text-xl font-bold">Rewards Center</h1>
      </header>
      <main class="flex-1 overflow-auto p-4">
        <div class="bg-white rounded-lg p-4 shadow mb-4">
          <h2 class="text-lg font-semibold mb-2">Your Points</h2>
          <p class="text-3xl font-bold text-green-500">1,250</p>
        </div>
        <h2 class="text-lg font-semibold mb-2">Available Rewards</h2>
        <ul class="space-y-4">
          <li class="bg-white rounded-lg p-4 shadow flex items-center justify-between">
            <div class="flex items-center">
              <GiftIcon class="h-8 w-8 text-purple-500 mr-3" />
              <div class="mb-4">
                <h3 class="font-semibold">$5 Gift Card</h3>
                <p class="text-sm text-gray-500">Local Eco-Store</p>
              </div>
            </div>
            <button class="bg-purple-500 text-white px-3 py-1 rounded-md text-sm">
              500 pts
            </button>
        </li>
        <li class="bg-white rounded-lg p-4 shadow flex items-center justify-between">
          <div class="flex items-center">
            <GiftIcon class="h-8 w-8 text-purple-500 mr-3 " />
            <div class="h-50%">
              <h3 class="font-semibold">Reusable Water Bottle</h3>
              <p class="text-sm text-gray-500">EcoConnect Branded</p>
            </div>
          </div>
          <button class="bg-purple-500 text-white px-3 py-1 rounded-md text-sm">
            750 pts
          </button>
        </li>
        <li class="bg-white rounded-lg p-4 shadow flex items-center justify-between">
          <div class="flex items-center">
            <GiftIcon class="h-8 w-8 text-purple-500 mr-3 " />
            <div class="h-50%">
              <h3 class="font-semibold">Reusable Water Bottle</h3>
              <p class="text-sm text-gray-500">EcoConnect Branded</p>
            </div>
          </div>
          <button class="bg-purple-500 text-white px-3 py-1 rounded-md text-sm">
            750 pts
          </button>
        </li>
        <li class="bg-white rounded-lg p-4 shadow flex items-center justify-between">
          <div class="flex items-center">
            <GiftIcon class="h-8 w-8 text-purple-500 mr-3 " />
            <div class="h-50%">
              <h3 class="font-semibold">Reusable Water Bottle</h3>
              <p class="text-sm text-gray-500">EcoConnect Branded</p>
            </div>
          </div>
          <button class="bg-purple-500 text-white px-3 py-1 rounded-md text-sm">
            750 pts
          </button>
        </li>
      </ul>
      
        </main>
    </div>
 
</template>