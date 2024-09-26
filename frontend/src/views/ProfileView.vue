<template>
    <div class="flex flex-col h-screen w-screen bg-green-50">
     <header class="p-4 bg-green-500 text-white flex items-center">
           <div Class="flex items-center">
             <ArrowLeftIcon Class="h-6 w-6 mr-2" />
             <h1 Class="text-xl font-bold">Profile</h1>
           </div>
           <SettingsIcon Class="h-6 w-6" />
         </header>
         <main Class="flex-1 overflow-auto p-4">
           <div Class="bg-white rounded-lg p-4 shadow mb-4 text-center">
             <img
               src="/img/placeholder.svg"
               alt="Profile"
               Class="w-24 h-24 rounded-full mx-auto mb-2"
             />
             <h2 Class="text-xl font-semibold">Jane Doe</h2>
             <p Class="text-gray-500">Eco Warrior</p>
           </div>
           <div Class="bg-white rounded-lg p-4 shadow mb-4">
             <h3 Class="text-lg font-semibold mb-2 flex items-center">
               <AwardIcon Class="h-5 w-5 mr-2 text-yellow-500" />
               Achievements
             </h3>
             <div Class="flex flex-wrap gap-2">
               <div Class="bg-gray-100 p-2 rounded-md text-sm">Paper Master</div>
               <div Class="bg-gray-100 p-2 rounded-md text-sm">Plastic Pro</div>
               <div Class="bg-gray-100 p-2 rounded-md text-sm">Glass Guru</div>
             </div>
           </div>
           <div Class="bg-white rounded-lg p-4 shadow">
             <h3 Class="text-lg font-semibold mb-2 flex items-center">
               <HistoryIcon Class="h-5 w-5 mr-2 text-blue-500" />
               Recycling History
             </h3>
             <ul Class="space-y-2">
               <li Class="flex justify-between items-center">
                 <span>Paper (2kg)</span>
                 <span Class="text-sm text-gray-500">2 days ago</span>
               </li>
               <li Class="flex justify-between items-center">
                 <span>Plastic (1kg)</span>
                 <span Class="text-sm text-gray-500">5 days ago</span>
               </li>
               <li Class="flex justify-between items-center">
                 <span>Glass (3kg)</span>
                 <span Class="text-sm text-gray-500">1 week ago</span>
               </li>
             </ul>
           </div>
         </main>
       </div>
     
   
   </template>

   <script setup>

</script>