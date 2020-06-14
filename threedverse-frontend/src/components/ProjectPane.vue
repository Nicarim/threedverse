<template>
  <div class="q-pa-sm project-pane">

    <div class="row q-pb-sm">
      <div class="col-auto q-pr-sm">
        <RoundAvatar/>
      </div>
      <div class="col author">
        <div>Project name tht</div>
        <div class="author-name">Marcin Gordziejewski</div>
      </div>
    </div>
    <div class="row">
      <div class="col background"></div>
    </div>
    <div class="open q-mt-sm">
      <q-btn flat color="primary" label="Open" to="/project/"/>
    </div>
  </div>
</template>

<!--
Ideas:
- background image might be what user chooses by default, but on hovering it should show unified view of 3 projections
- If multiple 3d models files are present - user should be able to click through all of them on the background pane using left/right arrows.
- ^ These shall only be auto generated projections
-->

<script>
import RoundAvatar from './RoundAvatar';

export default {
  name: 'ProjectPane',
  components: {RoundAvatar}
}
</script>

<style scoped lang="scss">
.project-pane {
  background-color: $blue-grey-1;
  border: 1px solid $blue-grey-3;
  width: 250px;
}

.author {
  display: flex;
  flex-direction: column;

  .author-name {
    font-size: 10px;
    font-weight: 300;
  }
}

.background {
  height: 180px;
  background-image: url('https://w.wallhaven.cc/full/md/wallhaven-md5z28.jpg');
  background-size: cover;
}

.open {
  text-align: center;
}
</style>
