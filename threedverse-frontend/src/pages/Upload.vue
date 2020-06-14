<template>
  <div class="q-pa-md">
    <q-form
      class="q-gutter-md"
    >
      <q-input
        filled
        label="Model Name"
      />

      <q-input
        filled
        label="Description"
        type="textarea"
        rows="12"
      />
      <q-file bottom-slots v-model="modelFiles" label="Select *.obj/*stl to upload" counter max-files="12">
        <template v-slot:before>
          <q-icon name="attachment"/>
        </template>

        <template v-slot:append>
          <q-icon v-if="modelFiles !== null" name="close" @click.stop="modelFiles = null" class="cursor-pointer"/>
          <q-icon name="search" @click.stop/>
        </template>

        <template v-slot:hint>
          Click on the field to select the files you want to upload. You can select multiple files.
        </template>
      </q-file>
      <q-file bottom-slots v-model="galleryFiles" label="Select *.png/*.jpg as images" counter max-files="1">
        <template v-slot:before>
          <q-icon name="image"/>
        </template>

        <template v-slot:append>
          <q-icon v-if="galleryFiles !== null" name="close" @click.stop="galleryFiles = null" class="cursor-pointer"/>
          <q-icon name="search" @click.stop/>
        </template>

        <template v-slot:hint>
          Click on the field to select the files you want to upload. You can select multiple files.
        </template>
      </q-file>
      <div>
        <q-btn label="Submit" type="submit" color="primary"/>
      </div>
    </q-form>
  </div>
</template>

<script>
export default {
  name: "Upload",
  data() {
    return {
      modelFiles: null,
      galleryFiles: null
    }
  }
}
</script>

<style scoped>

</style>
