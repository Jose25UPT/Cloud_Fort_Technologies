<template>
  <div>
    <!-- Navbar -->
    <Navbar />
    
    <!-- Main content sections -->
    <HeroSection />
    <AboutSection />
    <ServicesSection />
    <ProjectsSection />
    <ProcessSection />
    <ContactForm />
    <FooterSection />
  </div>
</template>

<script setup>
import Navbar from '@/components/Navbar.vue';
import HeroSection from '@/components/HeroSection.vue';
import AboutSection from '@/components/AboutSection.vue';
import ServicesSection from '@/components/ServicesSection.vue';
import ProjectsSection from '@/components/ProjectsSection.vue';
import ProcessSection from '@/components/ProcessSection.vue';
import ContactForm from '@/components/ContactForm.vue';
import FooterSection from '@/components/FooterSection.vue';
</script>

<style scoped>
html {
  scroll-behavior: smooth;
}

body {
  font-family: 'Inter', sans-serif;
  background-color: #000000;
  color: #FFFFFF;
  margin: 0;
}

section {
  width: 100%;
  padding-top: 80px;
}
</style>

