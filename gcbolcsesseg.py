import discord
import random
from discord_components import DiscordComponents, Button


async def main(msg, client):
    gandhi = [
        "Be the change that you wish to see in the world.",
        "Live as if you were to die tomorrow. Learn as if you were to live forever.",
        "An eye for an eye will only make the whole world blind.",
        "Happiness is when what you think, what you say, and what you do are in harmony.",
        "When I despair, I remember that all through history the way of truth and love have always won. There have been tyrants and murderers, and for a time, they can seem invincible, but in the end, they always fall. Think of it--always.",
        "The weak can never forgive. Forgiveness is the attribute of the strong.",
        "Where there is love there is life.",
        "Prayer is not asking. It is a longing of the soul. It is daily admission of one's weakness. It is better in prayer to have a heart without words than words without a heart.",
        "I like your Christ, I do not like your Christians. Your Christians are so unlike your Christ.",
        "Freedom is not worth having if it does not include the freedom to make mistakes.",
        "Nobody can hurt me without my permission.",
        "God has no religion.",
        "Hate the sin, love the sinner.",
        "I will not let anyone walk through my mind with their dirty feet.",
        "You must not lose faith in humanity. Humanity is like an ocean; if a few drops of the ocean are dirty, the ocean does not become dirty.",
        "The best way to find yourself is to lose yourself in the service of others.",
        "The future depends on what you do today.",
        "A man is but the product of his thoughts. What he thinks, he becomes.",
        "To give pleasure to a single heart by a single act is better than a thousand heads bowing in prayer.",
        "The greatness of a nation and its moral progress can be judged by the way its animals are treated.",
        "Man often becomes what he believes himself to be. If I keep on saying to myself that I cannot do a certain thing, it is possible that I may end by really becoming incapable of doing it. On the contrary, if I have the belief that I can do it, I shall surely acquire the capacity to do it even if I may not have it at the beginning.",
        "Each night, when I go to sleep, I die. And the next morning, when I wake up, I am reborn.",
        "Earth provides enough to satisfy every man's needs, but not every man's greed.",
        "What difference does it make to the dead, the orphans and the homeless, whether the mad destruction is wrought under the name of totalitarianism or in the holy name of liberty or democracy?",
        "To believe in something, and not to live it, is dishonest.",
        "There are people in the world so hungry, that God cannot appear to them except in the form of bread.",
        "It is unwise to be too sure of one's own wisdom. It is healthy to be reminded that the strongest might weaken and the wisest might err.",
        "Whatever you do will be insignificant, but it is very important that you do it.",
        # V 1.4.0-beta.1 V
        "The day the power of love overrules the love of power, the world will know peace.",
        "Truth never damages a cause that is just.",
        "Whenever you are confronted with an opponent. Conquer him with love.",
        "Strength does not come from physical capacity. It comes from an indomitable will",
        "It is easy enough to be friendly to one's friends. But to befriend the one who regards himself as your enemy is the quintessence of true religion. The other is mere business.",
        "Action expresses priorities.",
        "To call woman the weaker sex is a libel; it is man's injustice to woman. If by strength is meant brute strength, then, indeed, is woman less brute than man. If by strength is meant moral power, then woman is immeasurably man's superior. Has she not greater intuition, is she not more self-sacrificing, has she not greater powers of endurance, has she not greater courage? Without her, man could not be. If nonviolence is the law of our being, the future is with woman. Who can make a more effective appeal to the heart than woman?",
        "My Life is My Message",
        "It's the action, not the fruit of the action, that's important. You have to do the right thing. It may not be in your power, may not be in your time, that there'll be any fruit. But that doesn't mean you stop doing the right thing. You may never know what results come from your action. But if you do nothing, there will be no result.",
        "You don't know who is important to you until you actually lose them.",
        "I object to violence because when it appears to do good, the good is only temporary; the evil it does is permanent.",
        "You can chain me, you can torture me, you can even destroy this body, but you will never imprison my mind.",
        "If I had no sense of humor, I would long ago have committed suicide.",
        "You may never know what results come of your actions, but if you do nothing, there will be no results.",
        "There is more to life than simply increasing its speed.",
        "I offer you peace. I offer you love. I offer you friendship. I see your beauty. I hear your need. I feel your feelings.",
        "Love is the strongest force the world possesses and yet it is the humblest imaginable.",
        "The simplest acts of kindness are by far more powerful then a thousand heads bowing in prayer.",
        "Remember that all through history, there have been tyrants and murderers, and for a time, they seem invincible. But in the end, they always fall. Always.",
        "Silence becomes cowardice when occasion demands speaking out the whole truth and acting accordingly.",
        "There is nothing that wastes the body like worry, and one who has any faith in God should be ashamed to worry about anything whatsoever.",
        "They cannot take away our self respect if we do not give it to them.",
        "A coward is incapable of exhibiting love; it is the prerogative of the brave.",
        "In a gentle way, you can shake the world.",
        "Speak only if it improves upon the silence.",
        "There is no school equal to a decent home and no teacher equal to a virtuous parent.",
        "I cannot conceive of a greater loss than the loss of one's self-respect.",
        "To my mind, the life of a lamb is no less precious than that of a human being.",
        "In doing something, do it with love or never do it at all.",
        "I call him religious who understands the suffering of others."
    ]

    DiscordComponents(client)
    while True:
        try:
            quoteE = discord.Embed()
            quoteE.add_field(name="Bölcsesség Gandhi-tól", value=random.choice(gandhi))
            myMsg = await msg.channel.send(embed=quoteE, components=[Button(label="Idézz", style=1)])
            await client.wait_for("button_click", check=lambda i: i.component.label.startswith("Idézz"), timeout=56)
        except Exception:
            await myMsg.edit(embed=quoteE, components=[Button(label="Idézz", style=2, disabled=True)])
            break
        else:
            await myMsg.edit(embed=quoteE, components=[Button(label="Idézz", style=3, disabled=True)])
