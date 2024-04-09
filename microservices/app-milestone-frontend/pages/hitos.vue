<template>
  <div>
    <v-row>
      <br>
      <v-row class="mt-12"></v-row>
      <v-col cols="12" md="3">
        <v-text-field
          v-model="search"
          label="Buscar"
          outlined
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col>
        <v-row>
          <v-col cols="12" md="4" v-for="post in filteredPosts" :key="post.id">
            <v-card>
              <v-card-title>{{ post.titular }}</v-card-title>
              <v-card-subtitle>{{ post.fecha }}</v-card-subtitle>
              <v-card-text>{{ post.hecho }}</v-card-text>
              <v-card-actions>
                <v-chip-group
                  active-class="primary--text"
                  column
                >
                  <v-chip v-for="tag in post.tags.slice(1, -1).split(',').map(tag => tag.trim())" :key="tag">{{ tag.replace(/['"]/g, '') }}
                  </v-chip>
                </v-chip-group>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'Hitos',
  data () {
    return {
      posts: [],
      search: ''
    }
  },
  computed: {
    filteredPosts () {
      return this.search === '' ? this.posts : this.posts.filter(post => {
        return post.hecho.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  },
  async mounted () {
    try {
      const response = await fetch('http://poc-milestone.testea.top/gateway/questions')
      const data = await response.json()
      this.posts = data
    } catch (error) {
      console.log(error)
    }
  }
}
</script>

