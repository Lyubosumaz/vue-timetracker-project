<template>
  <v-container fluid>
    <template v-if="currentTab === 'tab-Reports'">
      <h1>Reports</h1>
      <v-layout>
        <v-flex>
          <h1>My reports</h1>
        </v-flex>
      </v-layout>

      <!-- :currentDay="day" -->
      <PersonalReports></PersonalReports>
    </template>
    <template v-if="currentTab === 'tab-Statistics'">
      <h1>Statistics</h1>
    </template>
  </v-container>
</template>

<script>
import Logo from "~/components/Logo.vue";
import VuetifyLogo from "~/components/VuetifyLogo.vue";
import PersonalReports from "~/components/table/PersonalReports.vue";

export default {
  components: {
    Logo,
    VuetifyLogo,
    PersonalReports,
  },
  props: {
    currentDay: {
      required: false,
      type: String,
      default: "",
    },
  },
  computed: {
    currentTab() {
      return "tab-Reports";
    },
  },
};
</script>
