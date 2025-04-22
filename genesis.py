#%%
# lista dos capitulos que srão baixados
mangaList = [
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-214/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-213/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-212/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-211/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-210/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-209/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-208/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-207/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-206/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-205/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-204/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-203/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-202/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-201/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-200/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-199/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-198/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-197/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-196/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-195-o-procedimento/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-194/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-193/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-192/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-191/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-190/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-189/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-188-5/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-188/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-187/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-186/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-185/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-184/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-183/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-182/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-181/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-180/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-179/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-178/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-177/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-176/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-175-1/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-174/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-173/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-172/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-171/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-170/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-169/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-168/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-167/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-166/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-165/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-164/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-163/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-162/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-161/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-160/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-159/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-158/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-157/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-156/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-155/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-154/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-153/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-152/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-151/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-150/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-149/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-148/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-147/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-146/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-145/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-144/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-143/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-142/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-141/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-140/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-139/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-138/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-137/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-136/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-135/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-134/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-133/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-132/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-131/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-130/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-129/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-128/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-127-resolve/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-126-perigo-e-divindades/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-125/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-124/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-123/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-122/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-121/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-120/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-119/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-118/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-117/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-116/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-115/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-114/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-113/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-112/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-111/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-110/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-109/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-108/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-107/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-106/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-105/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-104/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-103/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-102/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-101/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-100/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-99/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-98/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-97/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-96/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-95/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-94/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-93/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-92/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-91/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-90-a-lua/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-89-atencao/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-88/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-87-senhorita-presidente/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-86-bem-vindo-a-xyrus-academy/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-85-antecipacao/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-84-acordo-de-cavalheiros/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-83-um-baile/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-82-o-anuncio/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-81-diferente/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-80-um-frio-no-ar/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-79-revelacoes/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-78-nao-tao-legal/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-77-uma-mente-brilhante/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-76-dentro-do-nucleo/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-75-lar-doce-lar/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-74-precaucoes/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-73-audiencia/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-72-tempo-de-espera/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-71-fuga/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-70-resgate/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-69-elijah-cavaleiro/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-68/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-67/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-66/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-65/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-64/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-63/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-62/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-61-meu-time/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-60-idiota-romantico/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-59-confronto/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-58-primeiro-dia-de-trabalho/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-57-sentimentos-e-memorias-antigas/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-56-reuniao-de-familia/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-55-isso-vai-doer/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-54-torne-se-forte/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-53-uma-nova-geracao/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-52-breakpoint/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-51-alta-batalha/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-50-orgulho/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-49-o-exame/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-48-guilda-dos-aventureiros/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-47-feliz-aniversario/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-46-dawns-ballad/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-45-a-arma-perfeita/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-44-repercussoes/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-43-choque/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-42-para-o-reino/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-41-o-leilao/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-40-a-casa-de-leiloes/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-39-feliz-reencontro/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-38-5-notas-de-arthur-extra/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-38-1-notas-de-arthur-extra/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-38-melhorando/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-37-negocio/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-36-um-acordo/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-35-a-decisao/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-34-uma-demonstracao/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-33-dia-de-folga-do-arthur/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-32-expectativas/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-31-pai-e-filho/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-30-crescimento/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-29-lar/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-28-o-proximo-capitulo/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-27-a-pedra-de-sylvia/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-26-tres-anos-depois/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-25-o-que-esta-por-vir/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-24-o-outro-lado/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-23-ancia-rinia/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-22-anciao-virion/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-21-surge-um-desafio/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-20-o-reino-de-elenoir/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-19-mais-proximos/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-18-pra-la-e-pra-ca/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-17-reunindo-forca/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-16-caminho-a-percorrer/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-15-aqueles-que-sao-queridos/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-14-boa-companhia/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-13-sylvia/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-12-senhor-voz/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-11-seguindo-em-frente/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-10-uma-promessa/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-9-trabalho-em-equipe/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-8-emboscada/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-7-a-luta-de-treino/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-6-que-a-jornada-comece/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-5-o-nucleo-de-mana/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-4-quase-la/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-3-nao-sou-uma-mae-coruja/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-2-minha-nova-vida/",
"https://mugiwarasoficial.com/manga/the-beginning-after-the-end/chap-1-o-fim-do-tunel/",
]

# descomentar para bypassar os capitulos
# mangaList = []

# ordear mangaList
mangaList.sort()
#%%
# funções que serão usadas para baixar os mangás
import requests
import os
import time

def folderName(url):
    folder = url.split('/')[5].replace('.html','')
    num = folder.split('-')[1]
    znum = num.zfill(4)
    return folder.replace(f'-{num}',f'-{znum}')

def fileName(url):
    result = url.split('/')[9]
    print(result)
    return result

def getManga(manga):
    url = manga
    folder = folderName(url)
    print(folder)

    # criar pasta
    newpath = f'./{folder}'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    else:
        print('manga já baixado')
        return
    
    payload = {}
    headers = {}

    # Tentar novamente em caso de erro de conexão
    max_retries = 5
    retries = 0
    while retries < max_retries:
        try:
            response = requests.request("GET", url, headers=headers, data=payload)
            response.raise_for_status()  # Levanta uma exceção para códigos de status HTTP de erro
            break
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar {url}: {e}")
            retries += 1
            if retries < max_retries:
                print(f"Tentando novamente ({retries}/{max_retries}) em 1 segundo...")
                time.sleep(1)
            else:
                print("Número máximo de tentativas atingido. Pulando este manga.")
                return

    imagesRaw = response.text.split('data-src="')
    i = 0
    listRawImages = []
    for chunk in imagesRaw:
        if 'https://mugiwarasoficial.com/wp-content/uploads/WP-manga/data' in chunk:
            listRawImages.append(chunk.split('" class="wp')[0])
            print(f'imagens {str(i)}: {listRawImages[i]}')
            i += 1
    
    # baixar imagens
    for image in listRawImages:
        max_retries = 5
        retries = 0
        while retries < max_retries:
            try:
                img_data = requests.get(image).content
                break
            except requests.exceptions.RequestException as e:
                print(f"Erro ao baixar a imagem {image}: {e}")
                retries += 1
                if retries < max_retries:
                    print(f"Tentando novamente ({retries}/{max_retries}) em 1 segundo...")
                    time.sleep(1)
                else:
                    print(f"Falha ao baixar a imagem {image} após {max_retries} tentativas. Pulando...")
                    img_data = None
                    break

        if img_data:
            file = fileName(image)
            with open(f'./{folder}/{file}', 'wb') as handler:
                handler.write(img_data)

# return listImages
#%%

#%%
# loop para baixar os mangás

for manga in mangaList:
    getManga(manga)



# %%
# trata o nome das imagens
from os import listdir
from os.path import isfile, isdir, join

mypath = './'

onlyfolders = [f for f in listdir(mypath) if isdir(join(mypath, f))]
onlyfolders.sort()
print(onlyfolders)

for folder in onlyfolders:
    chapterFolder = f'./{folder}/'
    onlyfiles = [f for f in listdir(chapterFolder) if isfile(join(chapterFolder, f))]
    onlyfiles.sort()
    for file in onlyfiles:
        if len(file.split('.')[0]) <= 2:
            newfilename= file.replace(file.split('.')[0], file.split('.')[0].zfill(3))            
            os.rename(f'{chapterFolder}{file}', f'{chapterFolder}{newfilename}')
        if 'pagina_' in file or '-optimized' in file  or '-copiar' in file or '411409_' in file or '409788_' in file  or '430151_' in file:
            newfilename= file.replace('pagina_','').replace('-optimized','').replace('-copiar','').replace('411409_','').replace('409788_','').replace('430151_','')
            newfilename= newfilename.replace(newfilename.split('.')[0], newfilename.split('.')[0].zfill(3))            
            os.rename(f'{chapterFolder}{file}', f'{chapterFolder}{newfilename}')
    
    onlyfiles = [f for f in listdir(chapterFolder) if isfile(join(chapterFolder, f))]
    onlyfiles.sort()
    print(f'{folder}:{onlyfiles}')

# %%
# valida imagens
from os import listdir, lstat
from os.path import isfile, isdir, join

mypath = './'

onlyfolders = [f for f in listdir(mypath) if isdir(join(mypath, f))]
onlyfolders.sort()
print(onlyfolders)

for folder in onlyfolders:
    chapterFolder = f'./{folder}/'
    onlyfiles = [f for f in listdir(chapterFolder) if isfile(join(chapterFolder, f))]
    onlyfiles.sort()
    for file in onlyfiles:
        size = lstat(f'./{folder}/{file}').st_size
        if size == 0:
            # onlyfiles.remove(file)
            print(f'./{folder}/{file} size {size}')

    # print(f'{folder}:{onlyfiles}')



# %%
# cria os index.html
from os import listdir
from os.path import isfile, isdir, join, basename

mypath = './'

onlyfolders = [f for f in listdir(mypath) if isdir(join(mypath, f))]
onlyfolders.sort()
if '.git' in onlyfolders:
    onlyfolders.remove('.git')
print(onlyfolders)

# Obter o nome da pasta atual dinamicamente
folder_name = basename(os.getcwd())

# Print do nome da pasta
print(folder_name)

# Substituir "-" por espaço e deixar cada palavra com a primeira letra maiúscula
formatted_name = folder_name.replace("-", " ").title()
print(formatted_name)

titulo = formatted_name
conteudo = ''
for folder in onlyfolders:
    conteudo += f'<a href="/{folder_name}/{folder}/index.html">{folder}</a>'

with open('../liwrary/template-menu.html', 'r') as f:
    template = f.readlines()

for i in range(len(template)):
    template[i] = template[i].replace('--titulo-manga--', titulo).replace('<!--chapter-list-->', conteudo)

print('./index.html')
with open('./index.html', 'w') as f:
    f.writelines(template)
f.close()

for i in range(len(onlyfolders)):
    chapterFolder = f'./{onlyfolders[i]}/'
    anterior = f'/{folder_name}/'
    proximo = f'/{folder_name}/'
    menu = f'/{folder_name}/'
    if i - 1 >= 0: 
        anterior = f'/{folder_name}/{onlyfolders[i-1]}/'
    if i + 1 <= len(onlyfolders)-1: 
        proximo = f'/{folder_name}/{onlyfolders[i+1]}/'

    onlyfiles = [f for f in listdir(chapterFolder) if isfile(join(chapterFolder, f))]
    onlyfiles.sort()
    if 'readme.md' in onlyfiles:
        onlyfiles.remove('readme.md')
    if 'index.html' in onlyfiles:
        onlyfiles.remove('index.html')
    
    conteudo = ''

    for file in onlyfiles:
        conteudo += f'<img src="{file}"/>'

    
    with open('../liwrary/template-capitulo.html', 'r') as f:
        template = f.readlines()

    for x in range(len(template)):
        template[x] = template[x].replace('--titulo-manga--', titulo).replace('--capitulo--', onlyfolders[i]).replace('--proximoCapitulo.html--', proximo).replace('--capituloAnterior.html--', anterior).replace('--menu.html--', menu).replace('<!--manga-pages-->', conteudo)

    fileindex = f'{chapterFolder}index.html'
    print(fileindex)
    with open(fileindex, 'w') as f:
        f.writelines(template)
    f.close()


# %%


