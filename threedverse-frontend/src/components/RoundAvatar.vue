<template>
  <div class="round-avatar" v-bind:style="{ width: _size + 'px', height: _size + 'px' }"></div>
</template>

<script>
  export default {
    name: 'RoundAvatar',
    props: ['size'],
    data() {
      return {
        defaultSize: 30
      };
    },
    computed: {
      _size() {
        if (this.size === undefined) return this.defaultSize;
        return this.size;
      }
    }
  }
</script>

<style scoped>
  .round-avatar {
    background-image: url('https://cdn.thingiverse.com/renders/10/f3/5b/e3/59/49b3c65af9ea51fb5b9c3dc0181ac59e_thumb_medium.jpg');
    background-size: cover;
    position: relative;
    display: inline-block;
    border-radius: 100%;
  }
</style>
