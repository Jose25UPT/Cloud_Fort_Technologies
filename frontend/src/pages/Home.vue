<template>
  <div>
    <Navbar />
    <HeroSection />
    <ServicesSection />
    <AboutSection />
    <ProjectsSection />
    <ProcessSection />
    <ContactForm />
    <FooterSection />
  </div>
</template>

<script setup>
import Navbar from '@/components/Navbar.vue'
import HeroSection from '@/components/HeroSection.vue'
import ServicesSection from '@/components/ServicesSection.vue'
import AboutSection from '@/components/AboutSection.vue'
import ProjectsSection from '@/components/ProjectsSection.vue'
import ProcessSection from '@/components/ProcessSection.vue'
import ContactForm from '@/components/ContactForm.vue'
import FooterSection from '@/components/FooterSection.vue'
</script>

<style scoped>
html {
  scroll-behavior: smooth;
}

section {
  width: 100%;
  padding-top: 80px;
}
</style>

