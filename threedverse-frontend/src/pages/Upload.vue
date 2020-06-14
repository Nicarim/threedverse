<template>
  <div class="q-pa-md">
    <q-form
      class="q-gutter-md"
      @submit="onSubmit"
    >
      <q-input
        filled
        v-model="name"
        label="Model Name"
      />

      <q-input
        filled
        v-model="description"
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
        <q-btn label="Submit" type="submit" :color="color" :loading="submitting">
          <template v-slot:loading>
            <q-spinner-facebook/>
          </template>
        </q-btn>
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
      galleryFiles: null,
      description: null,
      name: null,
      color: "primary",
      submitting: false,
    }
  },
  methods: {
    onSubmit(evt) {
      this.submitting = true
      this.$axios.post('projects/', {
        name: this.name,
        description: this.description
      }).then((response) => {
        this.submitting = false
        this.name = null
        this.description = null
        this.$router.push('/project/')
      }).catch(() => {
        this.submitting = false
        this.color = 'negative'
        setTimeout(() => {
          this.color = 'primary'
        }, 1000)
      })
    }
  }
}
</script>

<style scoped>

</style>
