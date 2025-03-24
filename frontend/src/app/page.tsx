import Image from "next/image";
import Link from 'next/link';
import backgroundImage from '../../imgs/industrial.jpg';

export default function Home() {
  return (
    <div className="min-h-screen relative flex flex-col overflow-hidden">
      <div className="absolute inset-0 z-0">
        <div className="absolute inset-0 overflow-hidden">
          <Image
            src={backgroundImage}
            alt="Background"
            layout="fill"
            objectFit="cover"
            className="opacity-20 transform translate-x-0 transition-transform duration-[1000s] ease-linear infinite motion-safe:animate-slide"
          />
        </div>
        <div className="absolute inset-0 bg-teal-50 opacity-20"></div>
      </div>

      <nav className="bg-white shadow-md p-4 flex justify-between items-center relative z-10">
        <div className="font-bold text-xl text-blue-800">United Warehouses Ltd</div>
        <div className="flex gap-4">
          <Link href="/login" className="hover:text-blue-600 transition-colors duration-200">Login</Link>
          <Link href="/about" className="hover:text-blue-600 transition-colors duration-200">About Us</Link>
          <Link href="/contact" className="hover:text-blue-600 transition-colors duration-200">Contact Us</Link>
        </div>
      </nav>

      <main className="flex-grow flex items-center justify-center p-8 relative z-10">
        <div className="text-center max-w-2xl">
          <h1 className="text-4xl font-bold text-white mb-6">
            Empower Your Business with Instant Results
          </h1>
          <div className="flex flex-col sm:flex-row justify-center gap-4 mb-10">
            {/* <button className="bg-teal-600 hover:bg-teal-700 text-white font-bold py-3 px-6 rounded-full transition-colors duration-300">
              Get 
            </button> */}
            <button className="bg-transparent hover:bg-teal-100 text-teal-600 font-semibold py-3 px-6 rounded-full border border-teal-600 transition-colors duration-300">
            Started Now
            </button>
          </div>
          <div className="grid gap-8">
            <p className="text-lg text-white mb-8">
              Transform your business operations and see changes in real-time. We provide the tools you need to streamline processes and drive growth.
            </p>
          </div>
        </div>
      </main>

      <footer className="bg-white shadow-md p-4 flex gap-6 flex-wrap items-center justify-center text-sm text-gray-500 relative z-10">
        <a href="#" className="flex items-center gap-2 hover:text-blue-600 transition-colors duration-200">
          <Image src="/window.svg" alt="Window icon" width={16} height={16} aria-hidden />
          E-mail
        </a>
        <a href="#" className="flex items-center gap-2 hover:text-blue-600 transition-colors duration-200">
          <Image src="/globe.svg" alt="Globe icon" width={16} height={16} aria-hidden />
          united Warehouses Group →
        </a>
      </footer>
    </div>
  );
}