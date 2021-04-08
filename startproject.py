#!"C:\Python39\python.exe"

# IMPORTANT Change these variables depending on where you save projects and which editor you use
_PROJECT_DIRECTORY = "C:/Users/mitch/WebstormProjects/"
# .exe of prefered editor
_EDITOR = "webstorm64.exe"

import os
import sys
import re
import time

if len(sys.argv) == 3:
	raise Exception('Script only takes one arguments, no more, no less.')

# Gotta idiot proof this because I will be using it (makes sure project name is only letters, dashes and underscores)
if re.search('[a-zA-Z_\-]+', sys.argv[1]).group(0) != sys.argv[1]:
	raise Exception('Improper name for the project.')

os.chdir(_PROJECT_DIRECTORY)

os.system(f'vue create { sys.argv[1] }')
os.chdir(f'{ sys.argv[1] }/')
os.system('yarn add node-sass sass-loader@10.1.1 vue-router')
os.system('yarn add bulma')

# Go into the main directory to add main styling to project and update the main app
os.chdir('src/')

# Connects the main.scss file to the project
os.remove('main.js')

with open('main.js', 'w') as file:
	file.write("""import Vue from 'vue'
import Router from 'vue-router'
import App from './App.vue'
import Home from './pages/Home.vue'

Vue.use(Router)

Vue.config.productionTip = false

require('@/assets/main.scss');

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    }
  ]
})

new Vue({
  el: '#app',
  render: h => h(App),
  router
})""")

# Updates the current App.vue
os.remove('App.vue')

# Creates the new main app.vue page
with open('App.vue', 'w') as file:
	file.write("""<template>
  <div id="app">
    <navbar />
    <router-view></router-view>
  </div>
</template>

<script>
import navbar from './components/navbar.vue'

export default {
  name: 'App',
  components: {
    navbar,
  },
}
</script>""")

# Move to the assets folder to create the main styling sheet
os.chdir('assets/')

# Add Templated Styling
with open('main.scss', 'w') as file:
	# Template SCSS taken from https://justaashir.com/blog/bulma-vue-js-installation/
	file.write("""@charset "utf-8";

// Import a Google Font
@import url('https://fonts.googleapis.com/css?family=Nunito:400,700');

// Set your brand colors
$purple: #8A4D76;
$pink: #FA7C91;
$brown: #757763;
$beige-light: #D0D1CD;
$beige-lighter: #EFF0EB;

// Update Bulma's global variables
$family-sans-serif: 'Nunito', sans-serif;
$grey-dark: $brown;
$grey-light: $beige-light;
$primary: $purple;
$link: $pink;
$widescreen-enabled: false;
$fullhd-enabled: false;

// Update some of Bulma's component variables
$body-background-color: $beige-lighter;
$control-border-width: 2px;
$input-border-color: transparent;
$input-shadow: none;

// Import only what you need from Bulma
@import '../../node_modules/bulma/sass/utilities/_all.sass';
@import '../../node_modules/bulma/sass/base/_all.sass';
@import '../../node_modules/bulma/sass/elements/button.sass';
@import '../../node_modules/bulma/sass/elements/container.sass';
@import '../../node_modules/bulma/sass/elements/title.sass';
@import '../../node_modules/bulma/sass/form/_all.sass';
@import '../../node_modules/bulma/sass/components/navbar.sass';
@import '../../node_modules/bulma/sass/layout/hero.sass';
@import '../../node_modules/bulma/sass/layout/section.sass';
@import '../../node_modules/bulma/sass/helpers/_all.sass';
""")

# Move into the components folder to update the home page
os.chdir('../components')

# Deletes old home page to create new one
os.remove('HelloWorld.vue')

with open('navbar.vue', 'w') as file:
	file.write("""<template>
  <nav class="navbar box p-0 m-0" role="navigation" aria-label="main navigation">
    <div class="container">
      <div class="navbar-brand">
        <a
          role="button"
          class="navbar-burger"
          aria-label="menu"
          id="burger"
          aria-expanded="false"
          data-target="navbar"
          v-on:click="toggleBurger()"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbar" class="navbar-menu">
        <p class="navbar-item has-text-primary has-text-weight-bold">Insert App Name Here</p>
        <router-link class="navbar-item" to="/">Home</router-link>

        <div class="navbar-end">
          <router-link class="navbar-item is-primary" to="/">Contact</router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "navbar",
  props: {},
  methods: {
    toggleBurger: function () {
      document.getElementById("burger").classList.toggle("is-active");
      document.getElementById("navbar").classList.toggle("is-active");
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.navbar {
  border-radius: 0;
}
</style>
""")

# Create the pages directory
os.chdir('..')
os.mkdir('pages')
os.chdir('pages')

with open('Home.vue', 'w') as file:
	file.write("""<template>
  <div class="container">
    <h1>Hello World</h1>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
</style>""")

# Tell user that the script finished
os.system('cls')
print('Project Setup Finished :)')
time.sleep(2)
os.system('cls')

# Open the editor of choice defined at the top
os.system(_EDITOR + f" {os.path.join(_PROJECT_DIRECTORY, sys.argv[1])}")
