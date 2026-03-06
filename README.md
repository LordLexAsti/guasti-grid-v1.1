# guasti-grid-v1.1

Formalisation YAML/Markdown d'une architecture de responsabilité dans les systèmes de décision létale.

## Présentation

Ce dépôt propose une grammaire de la responsabilité pour les systèmes létaux assistés par logiciel, algorithme ou intelligence artificielle. Son idée directrice est simple : une machine peut participer à une chaîne causale, mais elle ne peut pas porter une responsabilité morale, politique ou juridique. Cette responsabilité reste humaine et institutionnelle.

L'objectif du projet est d'empêcher qu'un acte létal soit dilué dans une chaîne technique opaque où chacun n'aurait fait « qu'une petite partie » sans jamais répondre pleinement de la mort produite.

## Version philosophique utile

### Résumé ultra-court

Une machine ne peut pas être responsable d'un acte létal ; seuls des humains et des institutions peuvent l'être. Le projet propose donc une méthode pour examiner qui décide réellement, qui pouvait refuser, qui doit rendre des comptes, et qui doit réparation aux victimes.

### Le problème de départ

Quand une arme assistée par logiciel ou intelligence artificielle participe à une décision de tuer, une question revient immédiatement : qui répond de la mort ?

Le projet part d'un constat sobre : plus un système devient technique, rapide, distribué et opaque, plus il devient facile pour les acteurs humains de se retrancher derrière lui. Le risque n'est pas seulement l'erreur. Le risque est aussi la disparition apparente de l'auteur, comme si la complexité technique effaçait la responsabilité.

### L'idée centrale

Le cœur du projet consiste à refuser la dissolution de la responsabilité dans la technique. Une machine peut recommander, trier, signaler, accélérer ou exécuter une instruction. Elle ne peut pas répondre d'elle-même devant des victimes, une juridiction, une communauté politique ou l'humanité en général.

Le dépôt propose donc de remonter systématiquement l'acte létal vers son infrastructure humaine :
- le financeur,
- le concepteur,
- le gouvernement,
- le commandement,
- l'opérateur,
- et les victimes comme centre de la réparation.

## Points conceptuels essentiels

### 1. La machine n'est pas un sujet responsable

Le projet soutient qu'une IA n'est pas un nœud moral. Elle peut être causalement impliquée, mais elle ne peut ni répondre au sens fort, ni être jugée moralement, ni assumer une dette politique envers les victimes.

### 2. La responsabilité suppose une capacité réelle

La question décisive n'est pas seulement : y a-t-il un humain dans la boucle ?

La vraie question est : cet humain pouvait-il réellement dire non ?

Le projet distingue ici la capacité théorique et la capacité réelle. Si un opérateur agit sous pression extrême, avec une interface opaque, sans accès aux données brutes, sans temps de délibération et sans protection institutionnelle en cas de refus, alors sa responsabilité peut n'être qu'apparente. Dans ce cas, la responsabilité doit remonter vers les niveaux supérieurs qui ont conçu, imposé ou organisé la situation.

### 3. Une critique de la responsabilité cosmétique

Le dépôt critique l'idée selon laquelle la simple présence d'un humain suffirait à garantir une décision authentiquement humaine. Un humain peut être « dans la boucle » tout en ne disposant d'aucun pouvoir réel. Il peut alors servir de tampon de légitimation pour un système qu'il ne maîtrise pas.

### 4. Décision et réparation sont deux chaînes distinctes

Le projet distingue :
- la chaîne de décision, qui mène à l'acte,
- la chaîne de réparation, qui organise vérité, reconnaissance, compensation et réforme après l'acte.

Cette distinction permet de ne pas réduire la responsabilité à la seule désignation d'un coupable. Elle inclut aussi la manière dont les institutions doivent répondre aux victimes.

## Lecture critique

### Points forts

- Le projet refuse clairement la dilution de la responsabilité dans la complexité technique.
- Il introduit une distinction forte entre capacité formelle et capacité réelle.
- Il prend au sérieux le rôle de l'interface, du temps, de l'information et de la hiérarchie dans la décision.
- Il distingue utilement la production de l'acte et les obligations de réparation.
- Il formalise ses thèses, ce qui rend les désaccords plus visibles et discutables.

### Points de fragilité

- Plusieurs axiomes sont normatifs et non démontrés au sens strict.
- Les scores et seuils proposés peuvent donner une apparence de mesure exacte alors qu'ils doivent plutôt être lus comme des outils heuristiques.
- Les catégories d'acteurs simplifient parfois des réalités institutionnelles plus hybrides.
- L'idée d'une responsabilité devant « l'humanité » est moralement forte, mais politiquement et juridiquement contestable.

## Cartographie structurée du YAML

### 0. Table de référence
Lexique des acteurs, responsabilités, réparations et audiences.

### 1. Univers formel
Définit les ensembles de base : acteurs, types de responsabilité, formes de réparation, publics auxquels il faut répondre.

### 2. Nœuds
Décrit les acteurs comme porteurs de responsabilités, d'obligations de réparation et d'une capacité réelle à refuser ou rediriger l'action.

### 3. Machine non responsable
Pose l'exclusion de l'IA comme sujet moral ou juridique responsable.

### 4. Prédicat de responsabilité
Définit la responsabilité par trois conditions : être adressable, être imputable, et disposer d'une capacité réelle.

### 5. Axiomes
Structure l'ensemble : non-délégation à l'IA, impossibilité d'un acte létal sans responsable humain, double audience, seuil de capacité, ancrage interne et externe de l'obligation de répondre.

### 6. Graphes
Distingue graphe de décision et graphe de réparation.

### 7. Colonne de l'acte et complétude
Cherche à mesurer si la chaîne humaine de responsabilité est complète ou artificiellement tronquée.

### 8. Capacité réelle de l'opérateur
Analyse le temps, l'information, la hiérarchie, l'interface et les règles d'engagement comme conditions d'une décision réellement humaine.

### 9. Qualité de l'interface
Montre que le design de l'interface distribue concrètement le pouvoir de comprendre, d'hésiter, de refuser ou d'escalader.

### 10. Tempo opérationnel
Pense la dégradation des garanties de responsabilité selon le niveau d'intensité des opérations, sans jamais admettre la disparition complète d'un sujet responsable.

## Structure

- `guasti-grid.yaml` : formalisation complète en YAML/Markdown.
- `validate_yaml.py` : script simple de validation syntaxique YAML.

## Auteur

- **Alexandre Guasti** — *"Your Android"*

## Licence

Ce projet est sous licence **CC BY 4.0**.
