import React from "react";
import Navbar from "../components/landing_page/Navbar";
import HeroSection from "../components/landing_page/HeroSection";
import Footer from "../components/landing_page/Footer";

const HomePage = () => {
  return (
    <>
      <Navbar />
      <h1>Landing Page</h1>
      <HeroSection />
      <Footer />
    </>
  );
};

export default HomePage;
