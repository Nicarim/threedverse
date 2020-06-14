<template>
  <q-page>
    <div>
      <header class="text-h3 q-mb-sm">All Projects</header>
      <div class="q-pa-sm">
        <div class="row q-col-gutter-md">
          <div v-for="num in 10" :key="num" class="overflow-auto">
            <ProjectPane/>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
  import ProjectPane from '../components/ProjectPane';

  export default {
    name: 'ProjectList',
    components: {ProjectPane}
  }
</script>

<style scoped lang="scss">
</style>
