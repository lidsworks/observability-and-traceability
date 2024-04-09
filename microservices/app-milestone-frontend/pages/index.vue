<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card class="logo py-4 d-flex justify-center">
        <VuetifyLogo />
      </v-card>
      <v-divider class="my-4" />
      <v-card>
        <v-card-title>{{ post.titular }}</v-card-title>
        <v-card-subtitle>{{ post.fecha }}</v-card-subtitle>
        <v-card-text>{{ post.hecho }}</v-card-text>
        <v-card-actions>
          <v-chip-group
            active-class="primary--text"
            column
            v-if="post.tags"
          >
            <v-chip v-for="tag in post.tags.slice(1, -1).split(',').map(tag => tag.trim())" :key="tag">{{ tag.replace(/['"]/g, '') }}
            </v-chip>
          </v-chip-group>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'IndexPage',
  data () {
    return {
      post: []
    }
  },
  async mounted () {
    try {
      const response = await fetch('https://poc-milestone.testea.top/api/question/random')
      const data = await response.json()
      this.post = data
    } catch (error) {
      console.log(error)
    }
  }
}
</script>
