import type { ReactNode } from "react";

export const metadata = {
  title: "ThreatGuard AI",
  description: "Plataforma de detecção e resposta a ameaças com IA"
};

type RootLayoutProps = {
  children: ReactNode;
};

export default function RootLayout({ children }: RootLayoutProps) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}
