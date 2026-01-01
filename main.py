#!/usr/bin/env python3
"""
🏗️ TORRE HEBRON - YouTube Automation System
Versão: 1.2.0
"""

import sys
import os

# Adicionar módulos ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

def show_banner():
    """Exibe banner do sistema"""
    banner = """
    ╔══════════════════════════════════════╗
    ║         🏗️  TORRE HEBRON            ║
    ║    YouTube Automation System v1.2    ║
    ║          31/12/2025 - 01/01/2026     ║
    ╚══════════════════════════════════════╝
    """
    print(banner)

def main():
    """Função principal"""
    show_banner()
    
    print("🚀 Sistema inicializado!")
    print("\n📦 Módulos disponíveis:")
    print("  1. YouTube Automation")
    print("  2. Video Generator")
    print("  3. Thumbnail Creator")
    print("  4. Upload Manager")
    
    print("\n🎯 Use: python3 -m modules.youtube_automation")
    print("📁 GitHub: https://github.com/deegpnini/TorreHebron")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
