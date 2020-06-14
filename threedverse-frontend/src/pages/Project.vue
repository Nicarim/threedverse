<template>
  <q-page>
    <div class="row q-gutter-md">
      <div class="col">
        <div class="meta-row">
          <div class="q-mr-sm">
            <RoundAvatar size="50"/>
          </div>
          <div class="meta-title-row">
            <div class="project-name text-h5">Mechanical Quick Grab/Release Phone Stand</div>
            <div class="author-name text-caption">by Arron_mollet22 June 10, 2019</div>
          </div>
        </div>
        <div>
          <q-carousel v-model="slide" animated arrows navigation infinite>
            <q-carousel-slide :name="1" img-src="https://cdn.quasar.dev/img/mountains.jpg"/>
            <q-carousel-slide :name="2" img-src="https://cdn.quasar.dev/img/parallax1.jpg"/>
            <q-carousel-slide :name="3" img-src="https://cdn.quasar.dev/img/parallax2.jpg"/>
            <q-carousel-slide :name="4" img-src="https://cdn.quasar.dev/img/quasar.jpg"/>
          </q-carousel>
        </div>
      </div>
    </div>
    <div class="row q-mt-sm q-mb-sm">
      <q-btn color="secondary" label="Download"/>
    </div>
    <div class="row summary">
      <q-card
        style="width: 100%"
      >
        <q-tabs
          v-model="tab"
          dense
          class="text-grey"
          active-color="primary"
          indicator-color="primary"
          align="justify"
          narrow-indicator
        >
          <q-tab name="summary" label="Summary"/>
          <q-tab name="files" label="files"/>
        </q-tabs>
        <q-separator/>
        <q-tab-panels v-model="tab" animated>
          <q-tab-panel name="summary">
            <div class="">
              <div>
                <div class="ThingPage__description--14TtH"><p>This is a great design that I've dialed in and got working very
                  well. Looks great and is very functional. This stand allows multiple viewing angles and best of all has a
                  quick grab/release mechanism that grabs and locks the phone in when you let go and releases when you pick up
                  the phone. </p>
                  <p>This design currently works best for larger phones (iPhone 8 plus/XS Max size), but I am working on a
                    universal version, just need to get my hands on the smaller devises to test and dial it in.</p>
                  <p>The entire design is printable other than a small extension spring that needs to be installed when
                    putting the stand together.</p>
                  <p>5mm x 10mm extension springs work great and can be found in this kit for a great price:<br>
                    Spring Kit - <a rel="nofollow" href="https://amzn.to/2K4XJ6b">https://amzn.to/2K4XJ6b</a></p>
                  <b>Filament Used</b>
                  <p>All black part seen in pictures are an amazing PLA filament I print with often:<br>
                    Ziro Carbon fiber PLA - <a rel="nofollow" href="https://amzn.to/2K5xE79">https://amzn.to/2K5xE79</a></p>
                  <p>I'm printing with a Prusa i3 MK3s so I use Prusament a lot too. All orange filament seen is:<br>
                    Prusament Orange PETG - <a rel="nofollow" href="https://amzn.to/2Iva3tj">https://amzn.to/2Iva3tj</a></p>
                </div>
              </div>
            </div>
          </q-tab-panel>
          <q-tab-panel name="files">
            List of files
          </q-tab-panel>
        </q-tab-panels>
      </q-card>
    </div>
  </q-page>
</template>

<script>
  import RoundAvatar from '../components/RoundAvatar';

  export default {
    name: 'Project',
    components: {RoundAvatar},
    data() {
      return {
        slide: 1,
        tab: 'summary'
      }
    }
  }
</script>

<style scoped lang="scss">
  .meta-row {
    display: flex;
    flex-direction: row;
  }

  .meta-title-row {
    display: flex;
    flex-direction: column;

    .project-name {

    }

    .author-name {

    }
  }

  .summary {
    background-color: $grey-3;
  }
</style>
